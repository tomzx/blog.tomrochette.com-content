---

title: "Managed LLM Inference vs Self-Hosting: Where the Cost Breaks Even"
created: 2026-07-06
type: post
status: finished
tags: [llm, ai, infrastructure, cost-analysis, vllm, sglang, fireworks, bedrock, neocloud, nebius, lambda, coreweave, runpod, fully-ai-generated, llm=glm-5.2]
readability: 3
audience_notes: >
  Assumes the reader is an engineer or tech lead who has called an LLM API, understands dollars-per-token pricing, and knows roughly what a GPU and a batch are. No finance or ML-ops background required.
agent_sessions:
  - ses_0cab411e7ffeWBVFUXnyrcOFTS
---

You can serve an open model two ways.
You can pay someone else per token, through [Fireworks](https://www.fireworks.ai/pricing) or [Amazon Bedrock](https://aws.amazon.com/bedrock/pricing/), and never think about a GPU.
Or you can rent the GPU yourself, run [vLLM](https://docs.vllm.ai) or [SGLang](https://github.com/sgl-project/sglang), and pay for the hardware whether or not anyone is querying it.
**The choice is not really about which is cheaper per token.
It is about how much steady demand you have, because that single number decides which side of the break-even you land on.**

## The Two Price Lists

Managed inference sells you tokens, and the price is set by model size and provider.

On [Fireworks serverless](https://docs.fireworks.ai/serverless/pricing), a large dense model (above 16B parameters) runs a flat $0.90 per million tokens, while popular hosted models range from $0.15/$0.60 per million input/output for [gpt-oss-120b](https://docs.fireworks.ai/serverless/pricing) up to $1.74/$3.48 for [DeepSeek V4 Pro](https://docs.fireworks.ai/serverless/pricing).
[Amazon Bedrock](https://aws.amazon.com/bedrock/pricing/) tracks the same band, charging roughly $0.62/$1.85 for DeepSeek v3.2, $0.30/$1.20 for MiniMax M2, and about $0.15/$0.60 for the open gpt-oss-120b, near parity with Fireworks.
These two are effectively one market: the per-token price for the same open model moves together across providers, and the difference between them is rounding compared to the gap to raw hardware.

Self-hosting sells you time on a GPU, and that hourly rate now comes from three layers of providers, not one, each with a different price and a different amount of operational risk attached.
At the bottom are the **marketplace aggregators**, [RunPod](https://www.runpod.io/gpu-pricing) and [Vast.ai](https://www.vast.ai/pricing), which pool third-party hosts and run an 80GB H100 at roughly $3.29 per hour, falling further on interruptible instances; they are the cheapest option, but the machine behind the IP is someone else's, with inconsistent networking and thin compliance.
Above them sit the **neoclouds**, the purpose-built GPU clouds that actually own their datacenters, and here the prices are remarkably close while the substance is different: [Nebius](https://nebius.com/prices) runs an HGX H100 at $3.85 on-demand and $2.15 preemptible, [Lambda](https://lambda.ai/pricing) at about $3.99, and [CoreWeave](https://www.coreweave.com/pricing) around $6.16 for its inference-optimized tier, all with InfiniBand fabrics, known regions in the US and EU, and SOC 2 or HIPAA paperwork already completed.
The hyperscalers sit above that, at several dollars more per GPU with the full weight of enterprise procurement, and they are rarely the cheapest place to serve an open model.
**Notice the first asymmetry: none of these providers publishes a per-token cost that you can compare directly to managed pricing.
You have to convert the hourly rate into tokens yourself, and the conversion factor is throughput.**

## Converting Hardware Into Tokens

A GPU rental becomes a per-token price only once you know how many tokens the GPU can push per second under your load.
This is the number that determines everything, and it is why two teams can rent identical hardware and get very different costs.

A 70B-class dense model on a single H100, served with vLLM or SGLang in FP8 under heavy concurrent load, sustains somewhere in the range of 2,500 to 5,000 output tokens per second of aggregate throughput, with published numbers varying by context length, concurrency, and quantization.
Take 3,000 tokens per second as a defensible working figure.
At $3.29 per hour, that GPU fully saturated produces output tokens at roughly $0.30 per million, computed as the hourly rate divided by the 10.8 million tokens it generates in an hour.
**Set against Fireworks' $0.90 per million for a comparably sized model, a saturated self-hosted GPU is about three times cheaper per token, and against the cheaper Bedrock offerings it is still meaningfully ahead.**

That is the headline that pulls people toward self-hosting, and it is real, but it rests on one word: saturated.

## The Break-Even You Actually Care About

You do not pay for peak throughput, you pay for the hourly clock, and the clock runs whether the GPU is generating tokens or sitting idle waiting for the next request.
So the number that decides the decision is not peak tokens per second, it is your average sustained tokens per second over a full day.

The break-even is the average throughput at which self-hosting matches managed per-token pricing.
For an H100 at $3.29 per hour against Fireworks' $0.90 per million tokens, that break-even is about 1,000 tokens per second averaged across the day, which works out to roughly 88 million tokens per day or 2.6 billion tokens per month.
Below that average demand, managed is cheaper; above it, self-hosting wins, and the margin widens fast.
Expressed differently, 1,000 tokens per second is about one-third of the GPU's 3,000-token-per-second peak, so **you need to keep the GPU roughly a third utilized, sustained and averaged over every hour of every day, just to tie managed pricing on a 70B-class model.**

Three things move this line.
Cheaper managed pricing pushes the bar higher: against a $0.60-per-million managed model you need closer to 1,500 tokens per second average, about half of peak utilization, because each token you fail to generate costs you less on the managed side.
Cheaper GPU sourcing pushes the bar lower: the same H100 on [Nebius](https://nebius.com/prices) preemptible runs $2.15 instead of $3.29, which drops the break-even to about 660 tokens per second averaged, roughly a fifth of peak utilization, so a fault-tolerant batch workload willing to ride preemptible capacity can win on self-hosting at surprisingly low demand.
Larger models move it in your favor in absolute spend but demand much more hardware up front: a 671-billion-parameter mixture-of-experts model needs eight H200s or H100s, so the fixed monthly cost is eight times higher even though the managed per-token price is higher too, and the same utilization math decides who wins.
That eight-GPU case is also where the provider choice stops being interchangeable, because sharding a model across eight GPUs only pays off over a fast InfiniBand fabric, which the RunPod and Vast.ai marketplaces cannot reliably offer and the neoclouds like Nebius, Lambda, and CoreWeave were built around.
A single-GPU 70B can run anywhere cheap; a multi-GPU DeepSeek-class run is a neocloud or hyperscaler job, and the GPU price you plug into the break-even math should come from whichever tier can actually serve the model.

## The Middle Tier Someone Is Selling You

There is a third option that sits between the two, and it is worth naming because both providers push it.
[Fireworks on-demand](https://www.fireworks.ai/pricing) rents you a dedicated H100 for $7.00 per hour, about twice the raw [RunPod](https://www.runpod.io/gpu-pricing) rate, and [Bedrock Provisioned Throughput](https://aws.amazon.com/bedrock/pricing/) does the same on AWS with a commitment discount.
The premium buys you their tuned serving stack instead of vanilla vLLM, and Fireworks claims roughly 2.5x the throughput of the open-source engines on the same GPU.
If that holds, the effective per-token cost of their dedicated tier can approach or beat self-hosted vLLM, because you are paying more per hour but getting more tokens out of each hour.
**The catch is that the open engines are closing that performance gap quickly, so what you are increasingly paying for in the managed dedicated tier is not speed, it is the absence of an operations burden.**

## The Costs That Never Appear on the Invoice

The per-token and per-hour numbers are the easy part.
The real reason managed inference exists, and the real reason most teams should start there, is a set of costs that show up nowhere on either price list.

Self-hosting means someone has to deploy vLLM or SGLang, shard the model across GPUs, tune batching and KV-cache settings, handle OOM crashes, upgrade the engine every two weeks as it ships speedups, and keep the service alive at 3am when a node disappears.
It means there is no autoscaler by default, so spiky traffic forces a choice between idle GPUs burning money during troughs and latency spikes during peaks.
It means cold starts when weights reload, redundancy you have to build yourself for any production SLA, and security attestations you have to earn instead of inherit.
**Bedrock's per-token price quietly includes HIPAA, SOC 2, and region residency that a raw RunPod box does not, and for a regulated team that alone justifies the premium.**

This is the operations tax, and it is usually larger than the token markup.
A single engineer salary dwarfs the difference between $0.30 and $0.90 per million tokens for almost any sub-scale workload, which is another way of saying that self-hosting only looks cheap if you pretend engineering time is free.

## A Decision Rule

The choice collapses to how much steady, ideally batchable, demand you have and how much you value someone else carrying the operations load.

Stay on managed serverless when your traffic is low or spiky, your team is small, you rotate between many models, you need compliance handled for you, or you are still figuring out what to build.
The per-token premium is the price of scale-to-zero and zero ops, and for most early workloads it is the cheaper option even at a 3x token markup, because the GPU is rarely saturated enough to win.
**Roughly: if you move less than two to three billion tokens a month of a 70B-class model, managed serverless is almost certainly cheaper once you count anything for operations.**

Move to self-hosting when you have high, steady throughput that you can batch onto saturated GPUs, when you are running the same model for months, when the model is fine-tuned or custom, when privacy forces everything onto your own infrastructure, or when inference has become a large enough line item that a 3x cost difference materially changes the business.
Batch jobs that can fill a GPU to near 100% utilization are the cleanest win, because they turn the break-even math in your favor by definition.
Within self-hosting, the provider tier is its own choice: a single-GPU dev or batch job belongs on the cheapest marketplace (RunPod, Vast.ai) where a lost node just means a restart, while a multi-GPU production deployment or anything with compliance obligations belongs on a neocloud (Nebius, Lambda, CoreWeave) that owns the metal and can keep a sharded model together.

Use the managed dedicated tier, Fireworks on-demand or Bedrock Provisioned Throughput, for the awkward middle: enough steady traffic that serverless per-token is expensive, but not enough engineering bandwidth to run your own fleet well.
You pay a premium over raw hardware and give up some margin to the provider, and in exchange you keep predictable capacity without owning the pager.

## The Trend Underneath

The open inference engines are the reason this comparison is even close.
Two years ago the managed providers could charge a large premium because their serving stacks were meaningfully faster than anything you could run yourself.
vLLM and SGLang have erased most of that lead, with continuous batching, paged attention, prefix caching, and FP8 making a well-tuned open deployment competitive with proprietary platforms on the same silicon.
**As the performance gap closes, the managed premium is paying less for speed and more for the operations, scale, and compliance wrapped around the model, which means the real cost comparison is "tokens versus tokens plus an ops team," not "their engine versus yours."**

That is also why the providers keep moving up the stack, into fine-tuning, guardrails, agents, and evaluation, because the raw inference margin is compressing toward the cost of the GPU plus a thin layer of software.
For you, the buyer, that compression is good news: it means the decision gets simpler every quarter, and it comes down to one quantity you can measure, your own average sustained tokens per second, against one line, the hourly cost of a GPU you can keep busy.

## See also

- [Scaling the LLM Agent Company](../scaling-the-llm-agent-company/index.md) - the demand side of this question, why unit economics per inference call determine whether an agent business survives
- [Profit-as-a-Service](../profit-as-a-service/index.md) - managed inference as one more abstraction layer that takes a margin in exchange for removing an operations burden
- [Managing Many Concurrent LLM Agent Sessions](../managing-many-llm-agent-sessions/index.md) - the usage pattern that drives high, steady token throughput and tips the break-even toward self-hosting
- [Feature Parity Is Not a Moat](../feature-parity-is-not-a-moat/index.md) - the mechanism behind the closing performance gap, as vLLM and SGLang reach parity the inference-stack moat erodes

## References

- [Fireworks pricing](https://www.fireworks.ai/pricing) - serverless per-token and on-demand per-GPU-hour prices, including the $7.00/hr H100 and the ~2.5x throughput claim for their dedicated tier
- [Fireworks serverless pricing docs](https://docs.fireworks.ai/serverless/pricing) - the per-model input/cached/output token table used to anchor the managed side of the comparison
- [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/) - per-token prices for DeepSeek, MiniMax, Kimi, Gemma, and gpt-oss on AWS, plus Provisioned Throughput
- [RunPod GPU pricing](https://www.runpod.io/gpu-pricing) - raw on-demand hourly rates for H100, H200, B200, and A100 that anchor the self-hosted cost
- [Vast.ai pricing](https://www.vast.ai/pricing) - the supply-and-demand GPU marketplace, generally cheaper and lower guaranteed than RunPod
- [Nebius AI Cloud pricing](https://nebius.com/prices) - neocloud that owns its datacenters, H100 at $3.85 on-demand and $2.15 preemptible, with managed Token Factory inference on the same platform
- [Lambda pricing](https://lambda.ai/pricing) - neocloud with H100 instances around $3.99/GPU/hr and 1-Click multi-GPU clusters for large-model serving
- [CoreWeave pricing](https://www.coreweave.com/pricing) - enterprise neocloud with an inference-optimized H100 tier around $6.16/GPU/hr and spot pricing roughly half of that
- [vLLM documentation](https://docs.vllm.ai) - the open inference engine whose throughput figures set the self-hosted side of the equation
- [SGLang](https://github.com/sgl-project/sglang) - the other leading open serving stack, often faster on structured generation and prefix-heavy workloads
