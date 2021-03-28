---
title: Adding a class alias at boot time in Laravel
created: 2021-03-28
taxonomy:
  type: post
  status: draft
  category: Programming
  tag:
    - php
    - laravel
---

I make extensive use of [Laravel Debugbar](https://github.com/barryvdh/laravel-debugbar) to track performance of parts of my application. I sprinkle calls to `Debugbar::startMeasure` and `Debugbar::stopMeasure` to track the duration of certain segments of my code. However, when this code goes into production, this dependency isn't present. This cause the code to break since it cannot find `Debugbar` anymore.

```php
use Illuminate\Foundation\AliasLoader;
use My\SuperPackage\FooBar;

class ServiceProvider extends \Illuminate\Support\ServiceProvider
{
    public function register()
    {
        $this->app->booting(function() {
            $loader = AliasLoader::getInstance();
            $loader->alias('FooBar', FooBar::class);
        });
    }
}
```

# References
* https://laracasts.com/discuss/channels/laravel/dynamic-class-aliases-in-package
