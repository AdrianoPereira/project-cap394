rm -rf _book
Rscript -e "bookdown::render_book('index.Rmd', bookdown::gitbook(lib_dir = 'libs'))"
google-chrome _book/index.html
