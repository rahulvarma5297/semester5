#To convert tif into asc file (for future climate data)
library(raster)
f <- "C:/Users/Rahul Varma/Downloads/wc2.1_10m_tmin_MPI-ESM1-2-HR_ssp245_2081-2100.tif"
r <- raster(f)
ra <- aggregate(r, fact=2)  ## By default aggregates using mean, but see fun=
writeRaster(ra, "C:/Users/Rahul Varma/Downloads/tmin.asc", format="ascii")