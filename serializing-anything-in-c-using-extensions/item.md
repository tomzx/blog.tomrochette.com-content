---
title: Serializing "anything" in C# using extensions
date: 2011-06-05T04:22:07-05:00
Author: tomzx
Permalink: /serializing-anything-in-c-using-extensions/
taxonomy:
    type: post
    category: Programming
    tag: [c#, extensions, serialization]
---

I was recently interested in getting C# objects to serialize into XML so that I could save and load a configuration out of a file. Sadly, C# support for XML and serialization is far from the best stuff I've seen in programming. But anyway, here's what this post is about: using DataContract with a bit of extension magic to get anything to be serializable into XML!

One small problem when you use the Serializable attribute of C# is that you cannot serialize dictionary directly and we all know dictionaries are a VERY useful structure to have serialized. One easy way to have serializable dictionaries is to use the DataContract attribute instead. It implies a bit more code compared to the version where you use the Serializable attribute, but not that much more (mostly the WriteObject and ReadObject lines).

I haven't coded any of this, so thanks to user [Loudenvier][1] from [Stackoverflow.com][2]! This solution allows you to turn ANY object into an XML string representation. It also allows you to turn that string back into an object representation. Very useful.

<pre><code class="language-csharp line-numbers">public static class SerializationExtensions
{
    public static string Serialize&lt;T&gt;(this T obj)
    {
        var serializer = new DataContractSerializer(obj.GetType());
        using (var writer = new StringWriter())
        using (var stm = new XmlTextWriter(writer))
        {
            serializer.WriteObject(stm, obj);
            return writer.ToString();
        }
    }
    public static T Deserialize&lt;T&gt;(this string serialized)
    {
        var serializer = new DataContractSerializer(typeof(T));
        using (var reader = new StringReader(serialized))
        using (var stm = new XmlTextReader(reader))
        {
            return (T)serializer.ReadObject(stm);
        }
    }
}
</code></pre>

How to use example

<pre><code class="language-csharp line-numbers">// dictionary to serialize to string
Dictionary&lt;string, object&gt; myDict = new Dictionary&lt;string, object&gt;();
// add items to the dictionary...
myDict.Add(...);
// serialization is straight-forward
string serialized = myDict.Serialize();
...
// deserialization is just as simple
Dictionary&lt;string, object&gt; myDictCopy = serialized.Deserialize&lt;Dictionary&lt;string,object&gt;&gt;();
</code></pre>

**Source:** [http://www.stackoverflow.com][3]

 [1]: http://stackoverflow.com/users/285678/loudenvier
 [2]: http://www.stackoverflow.com
 [3]: http://www.stackoverflow.com/questions/1124597/why-isnt-there-an-xml-serializable-dictionary-in-net/5941122#5941122
