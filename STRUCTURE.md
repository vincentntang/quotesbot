Structure of the target HTML in JADE/PUG format. Uses bootstrap

```html
<div class="container">
  <div class="row header-box">
    <div class="col-md-8">
      <h1><a href="/" style="text-decoration: none;">Quotes to Scrape</a></h1>
    </div>
    <div class="col-md-4">
      <p><a href="/login">Login</a></p>
    </div>
  </div>
  <div class="row">
    <div class="col-md-8">
      <div class="quote" itemscope="" itemtype="http://schema.org/CreativeWork"><span class="text" itemprop="text">“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”</span><span>by <small class="author" itemprop="author">Albert Einstein</small><a href="/author/Albert-Einstein">(about)</a></span>
        <div class="tags">Tags:
          <meta class="keywords" itemprop="keywords" content="change,deep-thoughts,thinking,world" /><a class="tag" href="/tag/change/page/1/">change</a><a class="tag" href="/tag/deep-thoughts/page/1/">deep-thoughts</a><a class="tag" href="/tag/thinking/page/1/">thinking</a><a class="tag" href="/tag/world/page/1/">world</a>
        </div>
      </div>
      <div class="quote" itemscope="" itemtype="http://schema.org/CreativeWork"><span class="text" itemprop="text">“It is our choices, Harry, that show what we truly are, far more than our abilities.”</span><span>by <small class="author" itemprop="author">J.K. Rowling</small><a href="/author/J-K-Rowling">(about)</a></span>
        <div class="tags">Tags:
          <meta class="keywords" itemprop="keywords" content="abilities,choices" /><a class="tag" href="/tag/abilities/page/1/">abilities</a><a class="tag" href="/tag/choices/page/1/">choices</a>
        </div>
      </div>
      <!--etc -->
      <nav>
        <ul class="pager">
          <li class="next"><a href="/page/2/">Next <span aria-hidden="true">→</span></a></li>
        </ul>
      </nav>
    </div>
    <div class="col-md-4 tags-box">
      <h2>Top Ten tags</h2><span class="tag-item"><a class="tag" style="font-size: 28px;" href="/tag/love/">love</a></span><span class="tag-item"><a class="tag" style="font-size: 26px;" href="/tag/inspirational/">inspirational</a></span><span class="tag-item"><a class="tag" style="font-size: 26px;" href="/tag/life/">life</a></span><span class="tag-item"><a class="tag" style="font-size: 24px;" href="/tag/humor/">humor</a></span><span class="tag-item"><a class="tag" style="font-size: 22px;" href="/tag/books/">books</a></span><span class="tag-item"><a class="tag" style="font-size: 14px;" href="/tag/reading/">reading</a></span><span class="tag-item"><a class="tag" style="font-size: 10px;" href="/tag/friendship/">friendship</a></span><span class="tag-item"><a class="tag" style="font-size: 8px;" href="/tag/friends/">friends</a></span><span class="tag-item"><a class="tag" style="font-size: 8px;" href="/tag/truth/">truth</a></span><span class="tag-item"><a class="tag" style="font-size: 6px;" href="/tag/simile/">simile</a></span>
    </div>
  </div>
</div>
```


```jade
.container
  .row.header-box
    .col-md-8
      h1
        a(href='/', style='text-decoration: none') Quotes to Scrape
    .col-md-4
      p
        a(href='/login') Login
  .row
    .col-md-8
      .quote(itemscope='', itemtype='http://schema.org/CreativeWork')
        span.text(itemprop='text')
          | “The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”
        span
          | by 
          small.author(itemprop='author') Albert Einstein
          a(href='/author/Albert-Einstein') (about)
        .tags
          | Tags:
          meta.keywords(itemprop='keywords', content='change,deep-thoughts,thinking,world')
          a.tag(href='/tag/change/page/1/') change
          a.tag(href='/tag/deep-thoughts/page/1/') deep-thoughts
          a.tag(href='/tag/thinking/page/1/') thinking
          a.tag(href='/tag/world/page/1/') world
      .quote(itemscope='', itemtype='http://schema.org/CreativeWork')
        span.text(itemprop='text')
          | “It is our choices, Harry, that show what we truly are, far more than our abilities.”
        span
          | by 
          small.author(itemprop='author') J.K. Rowling
          a(href='/author/J-K-Rowling') (about)
        .tags
          | Tags:
          meta.keywords(itemprop='keywords', content='abilities,choices')
          a.tag(href='/tag/abilities/page/1/') abilities
          a.tag(href='/tag/choices/page/1/') choices
      //etc 
      nav
        ul.pager
          li.next
            a(href='/page/2/')
              | Next 
              span(aria-hidden='true') →
    .col-md-4.tags-box
      h2 Top Ten tags
      span.tag-item
        a.tag(style='font-size: 28px', href='/tag/love/') love
      span.tag-item
        a.tag(style='font-size: 26px', href='/tag/inspirational/') inspirational
      span.tag-item
        a.tag(style='font-size: 26px', href='/tag/life/') life
      span.tag-item
        a.tag(style='font-size: 24px', href='/tag/humor/') humor
      span.tag-item
        a.tag(style='font-size: 22px', href='/tag/books/') books
      span.tag-item
        a.tag(style='font-size: 14px', href='/tag/reading/') reading
      span.tag-item
        a.tag(style='font-size: 10px', href='/tag/friendship/') friendship
      span.tag-item
        a.tag(style='font-size: 8px', href='/tag/friends/') friends
      span.tag-item
        a.tag(style='font-size: 8px', href='/tag/truth/') truth
      span.tag-item
        a.tag(style='font-size: 6px', href='/tag/simile/') simile
```