# This is the OpenBazaar site

## Tips

## To run site locally

Install Jekyll by following these [instructions](https://jekyllrb.com/docs/installation/).

`bundle exec jekyll serve`

To preview drafts run with `--drafts` flag.

### Create a new draft

At the root of the project run:

`python create.py --title=example-title --date-2018-08-22`

### Include an embed youtube video

`{% include modules/embeded-video.html url="https://www.youtube.com/embed/92AOVPrm6MA" %}`

### To add captions

```
![](an-image.png)
*The image captions goes here, immediately afterwards*
```

### Markdown tips

Quick reference guide [here](https://gist.github.com/roachhd/779fa77e9b90fe945b0c)

