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

I make use of [Laravel Debugbar]()

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
