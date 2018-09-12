FROM rocker/r-ver:3.4.4

MAINTAINER "Frans van Dunné" frans@ixpantia.com

RUN apt-get update && apt-get -y install \
    libxml2-dev \
    r-cran-xml \
    libcurl4-openssl-dev \
    libssl-dev

# Instala packrat
RUN R -e 'install.packages("packrat", repos="http://cran.rstudio.com", dependencies=TRUE, lib="/usr/local/lib/R/site-library")'

COPY . /app
# Remueve cualquier binario local para que packrat use el codigo fuente
RUN rm -rf /app/packrat/lib*

WORKDIR /app

RUN R -e 'packrat::restore(project="/app")'

EXPOSE 9080

ENTRYPOINT ["Rscript"]
CMD ["arranca.R"]
