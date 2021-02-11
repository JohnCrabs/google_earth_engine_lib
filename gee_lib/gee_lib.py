import ee

# Try to Initialize Earth Engine API and if it fails Authentication is needed first.
try:
    ee.Initialize()
except:
    ee.Authenticate()
    ee.Initialize()

# -------------------------------------- #
# ---------- Table of Context ---------- #
# -------------------------------------- #
'''
1. Create Internal Variables
2. Create Variables
3. Create Internal Functions
4. Create Functions
5. Class
'''
# -------------------------------------- #

# -------------------------------------------------- #
# ---------- 1. Create Internal Variables ---------- #
# -------------------------------------------------- #

# ----------------------------------------- #
# ---------- 2. Create Variables ---------- #
# ----------------------------------------- #

'''
-----------------------------------
--- Dataset Acronyms Dictionary ---
-----------------------------------
--- A. ---
AER_AI = AERosol Index
AM     = Atmosphere Monthly
AR     = Agjusted Reflectance
-----------------------------------
--- B. ---
BAI  = Burn Area Index
BAM  = Burned Area Monthly
BRDF = Bidirectional Reflectance Distribution Function
-----------------------------------
--- C. ---
CO = Carbon Monoxide
-----------------------------------
--- D. ---
DS   = Dataset
-----------------------------------
--- E. ---
EFR  = Earth observation Full Resolution 
EVI  = Enchanced Vegetation Index
-----------------------------------
--- F. ---
FPAR = Fraction of Photosynthetically Active Radiation
-----------------------------------
--- G. ---
GRD = Ground Range Detected
GPP = Gross Primary Productivity
GSV = Global Static Variable
-----------------------------------
--- H. ---
HCHO = Formaldehyde
-----------------------------------
--- I. ---
-----------------------------------
--- J. ---
-----------------------------------
--- K. ---
-----------------------------------
--- L. ---
LAI  = Leaf Area Index
LCT  = Land Cover Type
LSTE = Land Surface Temperature and Emissivity
LWMD = Land Water Mask Derived
-----------------------------------
--- M. ---
MP  = Model Parameters
MSI = MultiSpectral Instrument
-----------------------------------
--- N. ---
NBRT = Normalized Burn Ratio Thermal
NDSI = Normalized Difference Snow Index
NDVI = Normalized Difference Vegetation Index
NDWI = Normalized Difference Water Index
NE   = Net Evapotranspiration
NO2  = Nitroxen Dioxide
NPP  = Net Primary Production
-----------------------------------
--- O. ---
O3   = Ozone
OFFL = OFFLine
OLCI = Ocean and Land Color Instrument
OR   = Ocean Reflectance
-----------------------------------
--- P. ---
POI  = Public Ortho Imagery
-----------------------------------
--- Q. ---
-----------------------------------
--- R. ---
RAW  = RAW images
-----------------------------------
--- S. ---
SAR  = Synthetic Aperture Radar
SC   = Snow Cover
SO2  = Sulphur Dioxide 
SR   = Surface Reflection
-----------------------------------
--- T. ---
TAF  = Thermal Anomalies and Fire
TOA  = Top Of Atmosphere
-----------------------------------
--- U. ---
-----------------------------------
--- V. ---
VI = Vegetation Indices
-----------------------------------
--- W. ---
-----------------------------------
--- X. ---
-----------------------------------
--- Y. ---
-----------------------------------
--- Z. ---
-----------------------------------
'''

# ----- SATELITE BANDS ----- #

GSV_DS_BAND_RED = "RED"
GSV_DS_BAND_BLUE = "BLUE"
GSV_DS_BAND_GREEN = "GREEN"
GSV_DS_BAND_NEAR_INFRARED = "NIR"
GSV_DS_BAND_SHORTWAVE_INFRARED_1 = "SWIR_1"
GSV_DS_BAND_SHORTWAVE_INFRARED_2 = "SWIR_2"
GSV_DS_BAND_THERMAL = "THERMAL"
GSV_DS_BAND_BRIGHTMESS_TEMPERATURE = "BRIGHTNES_TEMPERATURE"
GSV_DS_BAND_ATMOSPHERIC_OPACITY = "ATMOSHPERIC_OPACITY"
GSV_DS_BAND_CLOUD_QA = "CLOUD_QA"
GSV_DS_BAND_PIXEL_QA = "PIXEL_QA"
GSV_DS_BAND_RADSAT_QA = "RADSAT_QA"
GSV_DS_BAND_LANDSAT_BQA = "LANDSAT_BQA"

# ----- LANDSAT DATASETS ----- #

GSV_DS_LANDSAT_1_COLLECTION_ID = 'LANDSAT/LM01/C01/T1'
GSV_DS_LANDSAT_2_COLLECTION_ID = 'LANDSAT/LM02/C01/T1'
GSV_DS_LANDSAT_3_COLLECTION_ID = 'LANDSAT/LM03/C01/T1'
GSV_DS_LANDSAT_4_COLLECTION_ID = 'LANDSAT/LM04/C01/T1'
GSV_DS_LANDSAT_5_COLLECTION_ID = 'LANDSAT/LM05/C01/T1'
GSV_DS_LANDSAT_7_COLLECTION_ID = 'LANDSAT/LM07/C01/T1'
GSV_DS_LANDSAT_8_COLLECTION_ID = 'LANDSAT/LM08/C01/T1'

GSV_DS_LANDSAT_4_SR_COLLECTION_ID = "LANDSAT/LT04/C01/T1_SR"
GSV_DS_LANDSAT_4_TOA_COLLECTION_ID = "LANDSAT/LT04/C01/T1_TOA"
GSV_DS_LANDSAT_4_LT_RAW_COLLECTION_ID = "LANDSAT/LT04/C01/T1"

GSV_DS_LANDSAT_4_8DAY_BAI_COLLECTION_ID = "LANDSAT/LT04/C01/T1_8DAY_BAI"
GSV_DS_LANDSAT_4_8DAY_EVI_COLLECTION_ID = "LANDSAT/LT04/C01/T1_8DAY_EVI"
GSV_DS_LANDSAT_4_8DAY_NDVI_COLLECTION_ID = "LANDSAT/LT04/C01/T1_8DAY_NDVI"
GSV_DS_LANDSAT_4_8DAY_NBRT_COLLECTION_ID = "LANDSAT/LT04/C01/T1_8DAY_NBRT"
GSV_DS_LANDSAT_4_8DAY_NDSI_COLLECTION_ID = "LANDSAT/LT04/C01/T1_8DAY_NDSI"
GSV_DS_LANDSAT_4_8DAY_NDWI_COLLECTION_ID = "LANDSAT/LT04/C01/T1_8DAY_NDWI"

GSV_DS_LANDSAT_5_SR_COLLECTION_ID = "LANDSAT/LT05/C01/T1_SR"
GSV_DS_LANDSAT_5_TOA_COLLECTION_ID = "LANDSAT/LT05/C01/T1_TOA"
GSV_DS_LANDSAT_5_LT_RAW_COLLECTION_ID = "LANDSAT/LT05/C01/T1"

GSV_DS_LANDSAT_5_8DAY_BAI_COLLECTION_ID = "LANDSAT/LT05/C01/T1_8DAY_BAI"
GSV_DS_LANDSAT_5_8DAY_EVI_COLLECTION_ID = "LANDSAT/LT05/C01/T1_8DAY_EVI"
GSV_DS_LANDSAT_5_8DAY_NDVI_COLLECTION_ID = "LANDSAT/LT05/C01/T1_8DAY_NDVI"
GSV_DS_LANDSAT_5_8DAY_NBRT_COLLECTION_ID = "LANDSAT/LT05/C01/T1_8DAY_NBRT"
GSV_DS_LANDSAT_5_8DAY_NDSI_COLLECTION_ID = "LANDSAT/LT05/C01/T1_8DAY_NDSI"
GSV_DS_LANDSAT_5_8DAY_NDWI_COLLECTION_ID = "LANDSAT/LT05/C01/T1_8DAY_NDWI"

GSV_DS_LANDSAT_7_SR_COLLECTION_ID = "LANDSAT/LE07/C01/T1_SR"
GSV_DS_LANDSAT_7_TOA_COLLECTION_ID = "LANDSAT/LE07/C01/T1_TOA"
GSV_DS_LANDSAT_7_LT_RAW_COLLECTION_ID = "LANDSAT/LE07/C01/T1"

GSV_DS_LANDSAT_7_8DAY_BAI_COLLECTION_ID = "LANDSAT/LE07/C01/T1_8DAY_BAI"
GSV_DS_LANDSAT_7_8DAY_EVI_COLLECTION_ID = "LANDSAT/LE07/C01/T1_8DAY_EVI"
GSV_DS_LANDSAT_7_8DAY_NDVI_COLLECTION_ID = "LANDSAT/LE07/C01/T1_8DAY_NDVI"
GSV_DS_LANDSAT_7_8DAY_NBRT_COLLECTION_ID = "LANDSAT/LE07/C01/T1_8DAY_NBRT"
GSV_DS_LANDSAT_7_8DAY_NDSI_COLLECTION_ID = "LANDSAT/LE07/C01/T1_8DAY_NDSI"
GSV_DS_LANDSAT_7_8DAY_NDWI_COLLECTION_ID = "LANDSAT/LE07/C01/T1_8DAY_NDWI"

# ----- SENTINEL DATASETS ----- #

GSV_DS_SENTINEL_1_SAR_GRD = "COPERNICUS/S1_GRD"

GSV_DS_SENTINEL_2_MSI_TOA = "COPERNICUS/S2"
GSV_DS_SENTINEL_2_MSI_SR = "COPERNICUS/S2_SR"

GSV_DS_SENTINEL_3_OLCI_EFR = "COPERNICUS/S3/OLCI"

GSV_DS_SENTINEL_5_OFFL_AER_AI = "COPERNICUS/S5P/OFFL/L3_AER_AI"
GSV_DS_SENTINEL_5_OFFL_CLOUD = "COPERNICUS/S5P/OFFL/L3_CLOUD"
GSV_DS_SENTINEL_5_OFFL_CO = "COPERNICUS/S5P/OFFL/L3_CO"
GSV_DS_SENTINEL_5_OFFL_HCHO = "COPERNICUS/S5P/OFFL/L3_HCHO"
GSV_DS_SENTINEL_5_OFFL_NO2 = "COPERNICUS/S5P/OFFL/L3_NO2"
GSV_DS_SENTINEL_5_OFFL_O3 = "COPERNICUS/S5P/OFFL/L3_O3"
GSV_DS_SENTINEL_5_OFFL_SO2 = "COPERNICUS/S5P/OFFL/L3_SO2"
GSV_DS_SENTINEL_5_OFFL_CH4 = "COPERNICUS/S5P/OFFL/L3_CH4"

# ----- MODIS DATASETS ----- #

GSV_DS_MODIS_NADIR_BRDF_AR_DAILY_500 = "MODIS/006/MCD43A4"
GSV_DS_MODIS_ALBEDO_DAILY_QUALITY_500 = "MODIS/006/MCD43A3"
GSV_DS_MODIS_BRDF_ALBEDO_DAILY_GLOBAL_500 = "MODIS/006/MCD43A2"
GSV_DS_MODIS_TERRA_SR_DAILY_250 = "MODIS/006/MOD09GQ"
GSV_DS_MODIS_TERRA_SC_DAILY_500 = "MODIS/006/MOD10A1"
GSV_DS_MODIS_TERRA_LSTE_DAILY_GLOBAL_1000 = "MODIS/006/MOD11A1"
GSV_DS_MODIS_TERRA_SR_DAILY_GLOBAL_1000_500 = "MODIS/006/MOD09GA"
GSV_DS_MODIS_TERRA_OR_DAILY_GLOBAL_1000 = "MODIS/006/MODOCGA"
GSV_DS_MODIS_TERRA_TAF_DAILY_GLOBAL_1000 = "MODIS/006/MOD14A1"
GSV_DS_MODIS_BRDF_ALBEDO_MP_DAILY_500 = "MODIS/006/MCD43A1"
GSV_DS_MODIS_LAI_FPAR_4_DAY_GLOBAL_500 = "MODIS/006/MCD15A3H"
GSV_DS_MODIS_TERRA_SR_8_DAY_GLOBAL_250 = "MODIS/006/MOD09Q1"
GSV_DS_MODIS_TERRA_SR_8_DAY_GLOBAL_500 = "MODIS/006/MOD09A1"
GSV_DS_MODIS_TERRA_LSTE_8_DAY_GLOBAL_1000 = "MODIS/006/MOD11A2"
GSV_DS_MODIS_TERRA_TAF_8_DAY_GLOBAL_1000 = "MODIS/006/MOD14A2"
GSV_DS_MODIS_TERRA_GPP_8_DAY_GLOBAL_500 = "MODIS/006/MOD17A2H"
GSV_DS_MODIS_TERRA_NT_8_DAY_GLOBAL_500 = "MODIS/006/MOD16A2"
GSV_DS_MODIS_TERRA_VI_16_DAY_GLOBAL_250 = "MODIS/006/MOD13Q1"
GSV_DS_MODIS_TERRA_VI_16_DAY_GLOBAL_500 = "MODIS/006/MOD13A1"
GSV_DS_MODIS_TERRA_VI_16_DAY_GLOBAL_1000 = "MODIS/006/MOD13A2"
GSV_DS_MODIS_BAM_GLOBAL_500 = "MODIS/006/MCD64A1"
GSV_DS_MODIS_TERRA_AM_GLOBAL_PRODUCT = "MODIS/006/MOD08_M3"
GSV_DS_MODIS_LCT_YEARLY_GLOBAL_500 = "MODIS/006/MCD12Q1"
GSV_DS_MODIS_TERRA_NPP_YEARLY_GLOBAL_500 = "MODIS/006/MOD17A3H"
GSV_DS_MODIS_TERRA_LWMD_SRTM_YEARLY_GLOBAL_250 = "MODIS/006/MOD44W"

# ----- HIGH RESOLUTION IMAGERY ----- #

GSV_DS_PLANET_SKYSAT_POI_MULTISPECTRAL = "SKYSAT/GEN-A/PUBLIC/ORTHO/MULTISPECTRAL"
GSV_DS_PLANET_SKYSAT_POI_RGB = "SKYSAT/GEN-A/PUBLIC/ORTHO/RGB"
GSV_DS_NATIONAL_AGRICULTURE_IMAGERY_PROGRAM = "SKYSAT/GEN-A/PUBLIC/ORTHO/RGB"


# -------------------------------------------------- #
# ---------- 3. Create Internal Functions ---------- #
# -------------------------------------------------- #

# ----------------------------------------- #
# ---------- 4. Create Functions ---------- #
# ----------------------------------------- #

# ------------------------------ #
# ---------- 5. Class ---------- #
# ------------------------------ #

class GoogleEarthEngine:
    """
    This Class will be the core routine
    """
    def __init__(self):
        image_collection = None

    # ----- Print Functions (Debugging) ----- #

    def prt_image_collection(self):
        print(self.prt_image_collection())

    # ----- Core Functions ----- #

    def set_collection(self, collection_id, date_range, geometry):
        pass
