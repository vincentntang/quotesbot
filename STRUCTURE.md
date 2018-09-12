Structure of the target HTML in JADE/PUG format. Uses bootstrap

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