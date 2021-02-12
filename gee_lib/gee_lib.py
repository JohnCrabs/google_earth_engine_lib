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

_COLLECTION_ID_KEY = 'COLLECTION_ID'
_DATE_KEY = 'DATE'
_START_DATE_KEY = 'START_DATE'
_END_DATE_KEY = 'END_DATE'
_BANDS_KEY = 'BANDS'

# ----- SATELITE BANDS ----- #

_SINGLE_BAND_KEY = 'SINGLE_BAND'
_RED_KEY = 'RED'
_GREEN_KEY = 'GREEN'
_BLUE_KEY = 'BLUE'
_NIR_KEY = 'NIR'
_NIR_1_KEY = 'NIR_1'
_NIR_2_KEY = 'NIR_2'
_SWIR_1_KEY = 'SWIR_1'
_SWIR_2_KEY = 'SWIR_2'
_BQA_KEY = 'BQA'
_THERMAL_INFRARED_KEY = 'THERMAL_INFRARED'
_BRIGHTNESS_TEMPERATURE_1_KEY = 'BRIGHTNESS_TEMPERATURE_1'
_BRIGHTNESS_TEMPERATURE_2_KEY = 'BRIGHTNESS_TEMPERATURE_2'
_THERMAL_INFRARED_1_KEY = 'THERMAL_INFRARED_1'
_THERMAL_INFRARED_2_KEY = 'THERMAL_INFRARED_2'
_PANCHROMATIC_KEY = 'PANCHROMATIC'
_ULTRA_BLUE_KEY = 'ULTRA_BLUE'
_COASTAL_AEROSOL_KEY = 'COASTAL_AEROSOL'
_CIRRUS_KEY = 'CIRRUS'
_HH_KEY = 'HH'
_HV_KEY = 'HV'
_VV_KEY = 'VV'
_VH_KEY = 'VH'

_GEOMETRY_COUNTRY_COLLECTION = ee.FeatureCollection('users/midekisa/Countries')  # add countries boundary geometries

# ----- INDEXED ----- #
BAI_INDEX = 'BAI'
EVI_INDEX = 'EVI'
NDVI_INDEX = 'NDVI'
NBRT_INDEX = 'NBRT'
NDSI_INDEX = 'NDSI'
NDWI_INDEX = 'NDWI'

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
AMGP   = Atmosphere Monthly Global Product
AR     = Agjusted Reflectance
-----------------------------------
--- B. ---
BAI  = Burn Area Index
BAM  = Burned Area Monthly
BRDF = Bidirectional Reflectance Distribution Function
-----------------------------------
--- C. ---
CAMS = Copernicus Atmosphere Monitoring Services
CO = Carbon Monoxide
-----------------------------------
--- D. ---
DS   = DataSet
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
NCAR = National Center for Atmospheric Research
NCEP = National Centers for Environmental Prediction
NDSI = Normalized Difference Snow Index
NDVI = Normalized Difference Vegetation Index
NDWI = Normalized Difference Water Index
NE   = Net Evapotranspiration
NO2  = Nitroxen Dioxide
NPP  = Net Primary Production
NRT  = Near_Real_Time
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
RAW    = RAW images
RD  = Reabalysis Data
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
TOMS = Total Ozone Mapping Spectometer
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

# ----- LANDSAT DATASETS ----- #

GSV_DS_LANDSAT_1_T1_KEY = "LANDSAT_1_T1"
GSV_DS_LANDSAT_2_T1_KEY = "LANDSAT_2_T1"
GSV_DS_LANDSAT_3_T1_KEY = "LANDSAT_3_T1"

GSV_DS_LANDSAT_4_T1_KEY = "LANDSAT_4_T1"
GSV_DS_LANDSAT_4_SR_T1_KEY = "LANDSAT_4_SR_T1"
GSV_DS_LANDSAT_4_TOA_T1_KEY = "LANDSAT_4_TOA_T1"
GSV_DS_LANDSAT_4_RAW_T1_KEY = "LANDSAT_4_RAW_T1"
GSV_DS_LANDSAT_4_8DAY_BAI_KEY = "LANDSAT_4_8DAY_BAI_T1"
GSV_DS_LANDSAT_4_8DAY_EVI_KEY = "LANDSAT_4_8DAY_EVI_T1"
GSV_DS_LANDSAT_4_8DAY_NDVI_KEY = "LANDSAT_4_8DAY_NDVI_T1"
GSV_DS_LANDSAT_4_8DAY_NBRT_KEY = "LANDSAT_4_8DAY_NBRT_T1"
GSV_DS_LANDSAT_4_8DAY_NDSI_KEY = "LANDSAT_4_8DAY_NDSI_T1"
GSV_DS_LANDSAT_4_8DAY_NDWI_KEY = "LANDSAT_4_8DAY_NDWI_T1"

GSV_DS_LANDSAT_5_KEY = "LANDSAT_5"
GSV_DS_LANDSAT_5_SR_T1_KEY = "LANDSAT_5_SR_T1"
GSV_DS_LANDSAT_5_TOA_T1_KEY = "LANDSAT_5_TOA_T1"
GSV_DS_LANDSAT_5_RAW_T1_KEY = "LANDSAT_5_RAW_T1"
GSV_DS_LANDSAT_5_8DAY_BAI_KEY = "LANDSAT_5_8DAY_BAI_T1"
GSV_DS_LANDSAT_5_8DAY_EVI_KEY = "LANDSAT_5_8DAY_EVI_T1"
GSV_DS_LANDSAT_5_8DAY_NDVI_KEY = "LANDSAT_5_8DAY_NDVI_T1"
GSV_DS_LANDSAT_5_8DAY_NBRT_KEY = "LANDSAT_5_8DAY_NBRT_T1"
GSV_DS_LANDSAT_5_8DAY_NDSI_KEY = "LANDSAT_5_8DAY_NDSI_T1"
GSV_DS_LANDSAT_5_8DAY_NDWI_KEY = "LANDSAT_5_8DAY_NDWI_T1"

GSV_DS_LANDSAT_7_SR_T1_KEY = "LANDSAT_7_SR_T1"
GSV_DS_LANDSAT_7_TOA_T1_KEY = "LANDSAT_7_TOA_T1"
GSV_DS_LANDSAT_7_RAW_T1_KEY = "LANDSAT_7_RAW_T1"
GSV_DS_LANDSAT_7_8DAY_BAI_KEY = "LANDSAT_7_8DAY_BAI_T1"
GSV_DS_LANDSAT_7_8DAY_EVI_KEY = "LANDSAT_7_8DAY_EVI_T1"
GSV_DS_LANDSAT_7_8DAY_NDVI_KEY = "LANDSAT_7_8DAY_NDVI_T1"
GSV_DS_LANDSAT_7_8DAY_NBRT_KEY = "LANDSAT_7_8DAY_NBRT_T1"
GSV_DS_LANDSAT_7_8DAY_NDSI_KEY = "LANDSAT_7_8DAY_NDSI_T1"
GSV_DS_LANDSAT_7_8DAY_NDWI_KEY = "LANDSAT_7_8DAY_NDWI_T1"

GSV_DS_LANDSAT_8_SR_T1_KEY = "LANDSAT_8_SR_T1"
GSV_DS_LANDSAT_8_TOA_T1_KEY = "LANDSAT_8_TOA_T1"
GSV_DS_LANDSAT_8_RAW_T1_KEY = "LANDSAT_8_RAW_T1"
GSV_DS_LANDSAT_8_8DAY_BAI_KEY = "LANDSAT_8_8DAY_BAI_T1"
GSV_DS_LANDSAT_8_8DAY_EVI_KEY = "LANDSAT_8_8DAY_EVI_T1"
GSV_DS_LANDSAT_8_8DAY_NDVI_KEY = "LANDSAT_8_8DAY_NDVI_T1"
GSV_DS_LANDSAT_8_8DAY_NBRT_KEY = "LANDSAT_8_8DAY_NBRT_T1"
GSV_DS_LANDSAT_8_8DAY_NDSI_KEY = "LANDSAT_8_8DAY_NDSI_T1"
GSV_DS_LANDSAT_8_8DAY_NDWI_KEY = "LANDSAT_8_8DAY_NDWI_T1"

# ----- SENTINEL DATASETS ----- #

GSV_DS_SENTINEL_1_SAR_GRD_KEY = "SENTINEL_1_SAR_GRD"

GSV_DS_SENTINEL_2_MSI_TOA_COLLECTION_ID = "COPERNICUS/S2"
GSV_DS_SENTINEL_2_MSI_SR_COLLECTION_ID = "COPERNICUS/S2_SR"

GSV_DS_SENTINEL_3_OLCI_EFR_COLLECTION_ID = "COPERNICUS/S3/OLCI"

GSV_DS_SENTINEL_5_OFFL_AER_AI_COLLECTION_ID = "COPERNICUS/S5P/OFFL/L3_AER_AI"
GSV_DS_SENTINEL_5_OFFL_CLOUD_COLLECTION_ID = "COPERNICUS/S5P/OFFL/L3_CLOUD"
GSV_DS_SENTINEL_5_OFFL_CO_COLLECTION_ID = "COPERNICUS/S5P/OFFL/L3_CO"
GSV_DS_SENTINEL_5_OFFL_HCHO_COLLECTION_ID = "COPERNICUS/S5P/OFFL/L3_HCHO"
GSV_DS_SENTINEL_5_OFFL_NO2_COLLECTION_ID = "COPERNICUS/S5P/OFFL/L3_NO2"
GSV_DS_SENTINEL_5_OFFL_O3_COLLECTION_ID = "COPERNICUS/S5P/OFFL/L3_O3"
GSV_DS_SENTINEL_5_OFFL_SO2_COLLECTION_ID = "COPERNICUS/S5P/OFFL/L3_SO2"
GSV_DS_SENTINEL_5_OFFL_CH4_COLLECTION_ID = "COPERNICUS/S5P/OFFL/L3_CH4"

# ----- MODIS DATASETS ----- #

GSV_DS_MODIS_NADIR_BRDF_AR_DAILY_500_COLLECTION_ID = "MODIS/006/MCD43A4"
GSV_DS_MODIS_ALBEDO_DAILY_QUALITY_500_COLLECTION_ID = "MODIS/006/MCD43A3"
GSV_DS_MODIS_BRDF_ALBEDO_DAILY_GLOBAL_500_COLLECTION_ID = "MODIS/006/MCD43A2"
GSV_DS_MODIS_TERRA_SR_DAILY_250_COLLECTION_ID = "MODIS/006/MOD09GQ"
GSV_DS_MODIS_TERRA_SC_DAILY_500_COLLECTION_ID = "MODIS/006/MOD10A1"
GSV_DS_MODIS_TERRA_LSTE_DAILY_GLOBAL_1000_COLLECTION_ID = "MODIS/006/MOD11A1"
GSV_DS_MODIS_TERRA_SR_DAILY_GLOBAL_1000_500_COLLECTION_ID = "MODIS/006/MOD09GA"
GSV_DS_MODIS_TERRA_OR_DAILY_GLOBAL_1000_COLLECTION_ID = "MODIS/006/MODOCGA"
GSV_DS_MODIS_TERRA_TAF_DAILY_GLOBAL_1000_COLLECTION_ID = "MODIS/006/MOD14A1"
GSV_DS_MODIS_BRDF_ALBEDO_MP_DAILY_500_COLLECTION_ID = "MODIS/006/MCD43A1"
GSV_DS_MODIS_LAI_FPAR_4_DAY_GLOBAL_500_COLLECTION_ID = "MODIS/006/MCD15A3H"
GSV_DS_MODIS_TERRA_SR_8_DAY_GLOBAL_250_COLLECTION_ID = "MODIS/006/MOD09Q1"
GSV_DS_MODIS_TERRA_SR_8_DAY_GLOBAL_500_COLLECTION_ID = "MODIS/006/MOD09A1"
GSV_DS_MODIS_TERRA_LSTE_8_DAY_GLOBAL_1000_COLLECTION_ID = "MODIS/006/MOD11A2"
GSV_DS_MODIS_TERRA_TAF_8_DAY_GLOBAL_1000_COLLECTION_ID = "MODIS/006/MOD14A2"
GSV_DS_MODIS_TERRA_GPP_8_DAY_GLOBAL_500_COLLECTION_ID = "MODIS/006/MOD17A2H"
GSV_DS_MODIS_TERRA_NT_8_DAY_GLOBAL_500_COLLECTION_ID = "MODIS/006/MOD16A2"
GSV_DS_MODIS_TERRA_VI_16_DAY_GLOBAL_250_COLLECTION_ID = "MODIS/006/MOD13Q1"
GSV_DS_MODIS_TERRA_VI_16_DAY_GLOBAL_500_COLLECTION_ID = "MODIS/006/MOD13A1"
GSV_DS_MODIS_TERRA_VI_16_DAY_GLOBAL_1000_COLLECTION_ID = "MODIS/006/MOD13A2"
GSV_DS_MODIS_BAM_GLOBAL_500_COLLECTION_ID = "MODIS/006/MCD64A1"
GSV_DS_MODIS_TERRA_AM_GLOBAL_PRODUCT_COLLECTION_ID = "MODIS/006/MOD08_M3"
GSV_DS_MODIS_LCT_YEARLY_GLOBAL_500_COLLECTION_ID = "MODIS/006/MCD12Q1"
GSV_DS_MODIS_TERRA_NPP_YEARLY_GLOBAL_500_COLLECTION_ID = "MODIS/006/MOD17A3H"
GSV_DS_MODIS_TERRA_LWMD_SRTM_YEARLY_GLOBAL_250_COLLECTION_ID = "MODIS/006/MOD44W"

# ----- HIGH RESOLUTION IMAGERY ----- #

GSV_DS_PLANET_SKYSAT_POI_MULTISPECTRAL_COLLECTION_ID = "SKYSAT/GEN-A/PUBLIC/ORTHO/MULTISPECTRAL"
GSV_DS_PLANET_SKYSAT_POI_RGB_COLLECTION_ID = "SKYSAT/GEN-A/PUBLIC/ORTHO/RGB"
GSV_DS_NATIONAL_AGRICULTURE_IMAGERY_PROGRAM_COLLECTION_ID = "SKYSAT/GEN-A/PUBLIC/ORTHO/RGB"

# ----- ATMOSPHERIC ----- #

GSV_DS_CAMS_CLOBAL_NRT_COLLECTION_ID = "ECMWF/CAMS/NRT"
GSV_DS_MOD08_M3061_TERRA_AMGP_COLLECTION_ID = "MODIS/061/MOD08_M3"
GSV_DS_MYD08_M3061_AQUA_AMGP_COLLECTION_ID = "MODIS/061/MYD08_M3"
GSV_DS_NCEP_NCAR_RD_SEA_LEVEL_PRESSUR_COLLECTION_ID = "NCEP_RE/sea_level_pressure"
GSV_DS_NCEP_NCAR_RD_SURFACE_TEMPERATURE_COLLECTION_ID = "NCEP_RE/surface_temp"
GSV_DS_NCEP_NCAR_RD_WATER_VAPOR_COLLECTION_ID = "NCEP_RE/surface_wv"
GSV_DS_TOMS_OMI_MERGED_OZONE_DATA_COLLECTION_ID = "TOMS/MERGED"

DICT_FULL_DATASET = {
    GSV_DS_LANDSAT_1_T1_KEY: {  # LANDSAT 1 DATASET
        _COLLECTION_ID_KEY: 'LANDSAT/LM01/C01/T1',
        _DATE_KEY: {
            _START_DATE_KEY: '1972-07-23T00:00:00',
            _END_DATE_KEY: '1978-01-07T00:00:00'
        },
        _BANDS_KEY: {
            _GREEN_KEY: 'B4',
            _RED_KEY: 'B5',
            _NIR_1_KEY: 'B6',
            _NIR_2_KEY: 'B7',
            _BQA_KEY: 'BQA'
        }
    }, GSV_DS_LANDSAT_2_T1_KEY: {  # LANDSAT 2 DATASET
        _COLLECTION_ID_KEY: 'LANDSAT/LM02/C01/T1',
        _DATE_KEY: {
            _START_DATE_KEY: '1975-01-22T00:00:00',
            _END_DATE_KEY: '1982-02-26T00:00:00'
        },
        _BANDS_KEY: {
            _GREEN_KEY: 'B4',
            _RED_KEY: 'B5',
            _NIR_1_KEY: 'B6',
            _NIR_2_KEY: 'B7',
            _BQA_KEY: 'BQA'
        }
    }, GSV_DS_LANDSAT_3_T1_KEY: {  # LANDSAT 3 DATASET
        _COLLECTION_ID_KEY: 'LANDSAT/LM03/C01/T1',
        _DATE_KEY: {
            _START_DATE_KEY: '1978-03-05T00:00:00',
            _END_DATE_KEY: '1983-03-31T00:00:00'
        },
        _BANDS_KEY: {
            _GREEN_KEY: 'B4',
            _RED_KEY: 'B5',
            _NIR_1_KEY: 'B6',
            _NIR_2_KEY: 'B7',
            _BQA_KEY: 'BQA'
        }
    }, GSV_DS_LANDSAT_4_T1_KEY: {  # LANDSAT 4 DATASET
        _COLLECTION_ID_KEY: 'LANDSAT/LM04/C01/T1',
        _DATE_KEY: {
            _START_DATE_KEY: '1982-07-16T00:00:00',
            _END_DATE_KEY: '1993-12-14T00:00:00'
        },
        _BANDS_KEY: {
            _GREEN_KEY: 'B4',
            _RED_KEY: 'B5',
            _NIR_1_KEY: 'B6',
            _NIR_2_KEY: 'B7',
            _BQA_KEY: 'BQA'
        }
    }, GSV_DS_LANDSAT_4_SR_T1_KEY: {  # LANDSAT 4 SR T1
        _COLLECTION_ID_KEY: 'LANDSAT/LT04/C01/T1_SR',
        _DATE_KEY: {
            _START_DATE_KEY: '1984-03-01T00:00:00',
            _END_DATE_KEY: '2013-01-31T00:00:00'
        },
        _BANDS_KEY: {
            _BLUE_KEY: 'B1',
            _GREEN_KEY: 'B2',
            _RED_KEY: 'B3',
            _NIR_KEY: 'B4',
            _SWIR_1_KEY: 'B5',
            _THERMAL_INFRARED_KEY: 'B6',
            _SWIR_2_KEY: 'B7'
        }
    }, GSV_DS_LANDSAT_4_TOA_T1_KEY: {  # LANDSAT 4 SR TOA
        _COLLECTION_ID_KEY: 'LANDSAT/LT04/C01/T1_TOA',
        _DATE_KEY: {
            _START_DATE_KEY: '1984-03-01T00:00:00',
            _END_DATE_KEY: '2013-01-31T00:00:00'
        },
        _BANDS_KEY: {
            _BLUE_KEY: 'B1',
            _GREEN_KEY: 'B2',
            _RED_KEY: 'B3',
            _NIR_KEY: 'B4',
            _SWIR_1_KEY: 'B5',
            _THERMAL_INFRARED_KEY: 'B6',
            _SWIR_2_KEY: 'B7',
            _BQA_KEY: 'BQA'
        }
    }, GSV_DS_LANDSAT_4_RAW_T1_KEY: {  # LANDSAT 4 RAW
        _COLLECTION_ID_KEY: 'LANDSAT/LT04/C01/T1',
        _DATE_KEY: {
            _START_DATE_KEY: '1982-08-22T00:00:00',
            _END_DATE_KEY: '1982-08-22T00:00:00'
        },
        _BANDS_KEY: {
            _BLUE_KEY: 'B1',
            _GREEN_KEY: 'B2',
            _RED_KEY: 'B3',
            _NIR_KEY: 'B4',
            _SWIR_1_KEY: 'B5',
            _THERMAL_INFRARED_KEY: 'B6',
            _SWIR_2_KEY: 'B7',
            _BQA_KEY: 'BQA'
        }
    }, GSV_DS_LANDSAT_4_8DAY_BAI_KEY: {  # LANDSAT 4 BAI
        _COLLECTION_ID_KEY: 'LANDSAT/LT04/C01/T1_8DAY_BAI',
        _DATE_KEY: {
            _START_DATE_KEY: '1989-01-01',
            _END_DATE_KEY: '1992-12-31'
        },
        _BANDS_KEY: {
            _SINGLE_BAND_KEY: 'BAI'
        }
    }, GSV_DS_LANDSAT_4_8DAY_EVI_KEY: {  # LANDSAT 4 EVI
        _COLLECTION_ID_KEY: 'LANDSAT/LT04/C01/T1_8DAY_EVI',
        _DATE_KEY: {
            _START_DATE_KEY: '1989-01-01',
            _END_DATE_KEY: '1992-12-31'
        },
        _BANDS_KEY: {
            _SINGLE_BAND_KEY: 'EVI'
        }
    }, GSV_DS_LANDSAT_4_8DAY_NDVI_KEY: {  # LANDSAT 4 NDVI
        _COLLECTION_ID_KEY: 'LANDSAT/LT04/C01/T1_8DAY_NDVI',
        _DATE_KEY: {
            _START_DATE_KEY: '1989-01-01',
            _END_DATE_KEY: '1992-12-31'
        },
        _BANDS_KEY: {
            _SINGLE_BAND_KEY: 'NDVI'
        }
    }, GSV_DS_LANDSAT_4_8DAY_NBRT_KEY: {  # LANDSAT 4 NBRT
        _COLLECTION_ID_KEY: 'LANDSAT/LT04/C01/T1_8DAY_NBRT',
        _DATE_KEY: {
            _START_DATE_KEY: '1989-01-01',
            _END_DATE_KEY: '1992-12-31'
        },
        _BANDS_KEY: {
            _SINGLE_BAND_KEY: 'NBRT'
        }
    }, GSV_DS_LANDSAT_4_8DAY_NDSI_KEY: {  # LANDSAT 4 NDSI
        _COLLECTION_ID_KEY: 'LANDSAT/LT04/C01/T1_8DAY_NDSI',
        _DATE_KEY: {
            _START_DATE_KEY: '1989-01-01',
            _END_DATE_KEY: '1992-12-31'
        },
        _BANDS_KEY: {
            _SINGLE_BAND_KEY: 'NDSI'
        }
    }, GSV_DS_LANDSAT_4_8DAY_NDWI_KEY: {  # LANDSAT 4 NDWI
        _COLLECTION_ID_KEY: 'LANDSAT/LT04/C01/T1_8DAY_NDWI',
        _DATE_KEY: {
            _START_DATE_KEY: '1989-01-01',
            _END_DATE_KEY: '1992-12-31'
        },
        _BANDS_KEY: {
            _SINGLE_BAND_KEY: 'NDWI'
        }
    }, GSV_DS_LANDSAT_5_KEY: {  # LANDSAT 5
        _COLLECTION_ID_KEY: 'LANDSAT/LM05/C01/T1',
        _DATE_KEY: {
            _START_DATE_KEY: '1984-03-01T00:00:00',
            _END_DATE_KEY: '2013-01-31T00:00:00'
        },
        _BANDS_KEY: {
            _GREEN_KEY: 'B4',
            _RED_KEY: 'B5',
            _NIR_1_KEY: 'B6',
            _NIR_2_KEY: 'B7',
            _BQA_KEY: 'BQA'
        }
    }, GSV_DS_LANDSAT_5_SR_T1_KEY: {  # LANDSAT 5 SR T1
        _COLLECTION_ID_KEY: 'LANDSAT/LT05/C01/T1_SR',
        _DATE_KEY: {
            _START_DATE_KEY: '1984-01-01T00:00:00',
            _END_DATE_KEY: '2012-05-05T00:00:00'
        },
        _BANDS_KEY: {
            _BLUE_KEY: 'B1',
            _GREEN_KEY: 'B2',
            _RED_KEY: 'B3',
            _NIR_KEY: 'B4',
            _SWIR_1_KEY: 'B5',
            _THERMAL_INFRARED_KEY: 'B6',
            _SWIR_2_KEY: 'B7'
        }
    }, GSV_DS_LANDSAT_5_TOA_T1_KEY: {  # LANDSAT 5 SR TOA
        _COLLECTION_ID_KEY: 'LANDSAT/LT05/C01/T1_TOA',
        _DATE_KEY: {
            _START_DATE_KEY: '1984-01-01T00:00:00',
            _END_DATE_KEY: '2012-05-05T00:00:00'
        },
        _BANDS_KEY: {
            _BLUE_KEY: 'B1',
            _GREEN_KEY: 'B2',
            _RED_KEY: 'B3',
            _NIR_KEY: 'B4',
            _SWIR_1_KEY: 'B5',
            _THERMAL_INFRARED_KEY: 'B6',
            _SWIR_2_KEY: 'B7',
            _BQA_KEY: 'BQA'
        }
    }, GSV_DS_LANDSAT_5_RAW_T1_KEY: {  # LANDSAT 5 RAW
        _COLLECTION_ID_KEY: 'LANDSAT/LT05/C01/T1',
        _DATE_KEY: {
            _START_DATE_KEY: '1984-01-01T00:00:00',
            _END_DATE_KEY: '2012-05-05T00:00:00'
        },
        _BANDS_KEY: {
            _BLUE_KEY: 'B1',
            _GREEN_KEY: 'B2',
            _RED_KEY: 'B3',
            _NIR_KEY: 'B4',
            _SWIR_1_KEY: 'B5',
            _THERMAL_INFRARED_KEY: 'B6',
            _SWIR_2_KEY: 'B7',
            _BQA_KEY: 'BQA'
        }
    }, GSV_DS_LANDSAT_5_8DAY_BAI_KEY: {  # LANDSAT 5 BAI
        _COLLECTION_ID_KEY: 'LANDSAT/LT05/C01/T1_8DAY_BAI',
        _DATE_KEY: {
            _START_DATE_KEY: '2011-01-01',
            _END_DATE_KEY: '2011-12-31'
        },
        _BANDS_KEY: {
            _SINGLE_BAND_KEY: 'BAI'
        }
    }, GSV_DS_LANDSAT_5_8DAY_EVI_KEY: {  # LANDSAT 5 EVI
        _COLLECTION_ID_KEY: 'LANDSAT/LT05/C01/T1_8DAY_EVI',
        _DATE_KEY: {
            _START_DATE_KEY: '2011-01-01',
            _END_DATE_KEY: '2011-12-31'
        },
        _BANDS_KEY: {
            _SINGLE_BAND_KEY: 'EVI'
        }
    }, GSV_DS_LANDSAT_5_8DAY_NDVI_KEY: {  # LANDSAT 5 NDVI
        _COLLECTION_ID_KEY: 'LANDSAT/LT05/C01/T1_8DAY_NDVI',
        _DATE_KEY: {
            _START_DATE_KEY: '2011-01-01',
            _END_DATE_KEY: '2011-12-31'
        },
        _BANDS_KEY: {
            _SINGLE_BAND_KEY: 'NDVI'
        }
    }, GSV_DS_LANDSAT_5_8DAY_NBRT_KEY: {  # LANDSAT 5 NBRT
        _COLLECTION_ID_KEY: 'LANDSAT/LT05/C01/T1_8DAY_NBRT',
        _DATE_KEY: {
            _START_DATE_KEY: '2011-01-01',
            _END_DATE_KEY: '2011-12-31'
        },
        _BANDS_KEY: {
            _SINGLE_BAND_KEY: 'NBRT'
        }
    }, GSV_DS_LANDSAT_5_8DAY_NDSI_KEY: {  # LANDSAT 5 NDSI
        _COLLECTION_ID_KEY: 'LANDSAT/LT05/C01/T1_8DAY_NDSI',
        _DATE_KEY: {
            _START_DATE_KEY: '2011-01-01',
            _END_DATE_KEY: '2011-12-31'
        },
        _BANDS_KEY: {
            _SINGLE_BAND_KEY: 'NDSI'
        }
    }, GSV_DS_LANDSAT_5_8DAY_NDWI_KEY: {  # LANDSAT 5 NDWI
        _COLLECTION_ID_KEY: 'LANDSAT/LT05/C01/T1_8DAY_NDWI',
        _DATE_KEY: {
            _START_DATE_KEY: '2011-01-01',
            _END_DATE_KEY: '2011-12-31'
        },
        _BANDS_KEY: {
            _SINGLE_BAND_KEY: 'NDWI'
        }
    }, GSV_DS_LANDSAT_7_SR_T1_KEY: {  # LANDSAT 7 SR T1
        _COLLECTION_ID_KEY: 'LANDSAT/LE07/C01/T1_SR',
        _DATE_KEY: {
            _START_DATE_KEY: '1999-01-01T00:00:00',
            _END_DATE_KEY: '2021-01-13T00:00:00'
        },
        _BANDS_KEY: {
            _BLUE_KEY: 'B1',
            _GREEN_KEY: 'B2',
            _RED_KEY: 'B3',
            _NIR_KEY: 'B4',
            _SWIR_1_KEY: 'B5',
            _THERMAL_INFRARED_KEY: 'B6',
            _SWIR_2_KEY: 'B7'
        }
    }, GSV_DS_LANDSAT_7_TOA_T1_KEY: {  # LANDSAT 7 SR TOA
        _COLLECTION_ID_KEY: 'LANDSAT/LE07/C01/T1_TOA',
        _DATE_KEY: {
            _START_DATE_KEY: '1999-01-01T00:00:00',
            _END_DATE_KEY: '2021-01-15T00:00:00'
        },
        _BANDS_KEY: {
            _BLUE_KEY: 'B1',
            _GREEN_KEY: 'B2',
            _RED_KEY: 'B3',
            _NIR_KEY: 'B4',
            _SWIR_1_KEY: 'B5',
            _THERMAL_INFRARED_1_KEY: 'B6_VCID_1',
            _THERMAL_INFRARED_2_KEY: 'B6_VCID_2',
            _SWIR_2_KEY: 'B7',
            _PANCHROMATIC_KEY: 'B8',
            _BQA_KEY: 'BQA'
        }
    }, GSV_DS_LANDSAT_7_RAW_T1_KEY: {  # LANDSAT 7 RAW
        _COLLECTION_ID_KEY: 'LANDSAT/LE07/C01/T1',
        _DATE_KEY: {
            _START_DATE_KEY: '1999-01-01T00:00:00',
            _END_DATE_KEY: '2021-01-15T00:00:00'
        },
        _BANDS_KEY: {
            _BLUE_KEY: 'B1',
            _GREEN_KEY: 'B2',
            _RED_KEY: 'B3',
            _NIR_KEY: 'B4',
            _SWIR_1_KEY: 'B5',
            _THERMAL_INFRARED_1_KEY: 'B6_VCID_1',
            _THERMAL_INFRARED_2_KEY: 'B6_VCID_2',
            _SWIR_2_KEY: 'B7',
            _PANCHROMATIC_KEY: 'B8',
            _BQA_KEY: 'BQA'
        }
    }, GSV_DS_LANDSAT_7_8DAY_BAI_KEY: {  # LANDSAT 7 BAI
        _COLLECTION_ID_KEY: 'LANDSAT/LE07/C01/T1_8DAY_BAI',
        _DATE_KEY: {
            _START_DATE_KEY: '1999-01-01',
            _END_DATE_KEY: '2002-12-31'
        },
        _BANDS_KEY: {
            _SINGLE_BAND_KEY: 'BAI'
        }
    }, GSV_DS_LANDSAT_7_8DAY_EVI_KEY: {  # LANDSAT 7 EVI
        _COLLECTION_ID_KEY: 'LANDSAT/LE07/C01/T1_8DAY_EVI',
        _DATE_KEY: {
            _START_DATE_KEY: '1999-01-01',
            _END_DATE_KEY: '2002-12-31'
        },
        _BANDS_KEY: {
            _SINGLE_BAND_KEY: 'EVI'
        }
    }, GSV_DS_LANDSAT_7_8DAY_NDVI_KEY: {  # LANDSAT 7 NDVI
        _COLLECTION_ID_KEY: 'LANDSAT/LE07/C01/T1_8DAY_NDVI',
        _DATE_KEY: {
            _START_DATE_KEY: '1999-01-01',
            _END_DATE_KEY: '2002-12-31'
        },
        _BANDS_KEY: {
            _SINGLE_BAND_KEY: 'NDVI'
        }
    }, GSV_DS_LANDSAT_7_8DAY_NBRT_KEY: {  # LANDSAT 7 NBRT
        _COLLECTION_ID_KEY: 'LANDSAT/LE07/C01/T1_8DAY_NBRT',
        _DATE_KEY: {
            _START_DATE_KEY: '1999-01-01',
            _END_DATE_KEY: '2002-12-31'
        },
        _BANDS_KEY: {
            _SINGLE_BAND_KEY: 'NBRT'
        }
    }, GSV_DS_LANDSAT_7_8DAY_NDSI_KEY: {  # LANDSAT 7 NDSI
        _COLLECTION_ID_KEY: 'LANDSAT/LE07/C01/T1_8DAY_NDSI',
        _DATE_KEY: {
            _START_DATE_KEY: '1999-01-01',
            _END_DATE_KEY: '2002-12-31'
        },
        _BANDS_KEY: {
            _SINGLE_BAND_KEY: 'NDSI'
        }
    }, GSV_DS_LANDSAT_7_8DAY_NDWI_KEY: {  # LANDSAT 7 NDWI
        _COLLECTION_ID_KEY: 'LANDSAT/LE07/C01/T1_8DAY_NDWI',
        _DATE_KEY: {
            _START_DATE_KEY: '1999-01-01',
            _END_DATE_KEY: '2002-12-31'
        },
        _BANDS_KEY: {
            _SINGLE_BAND_KEY: 'NDWI'
        }
    }, GSV_DS_LANDSAT_8_SR_T1_KEY: {  # LANDSAT 8 SR T1
        _COLLECTION_ID_KEY: 'LANDSAT/LC08/C01/T1_SR',
        _DATE_KEY: {
            _START_DATE_KEY: '2013-04-11T00:00:00',
            _END_DATE_KEY: '2021-01-22T00:00:00'
        },
        _BANDS_KEY: {
            _ULTRA_BLUE_KEY: 'B1',
            _BLUE_KEY: 'B2',
            _GREEN_KEY: 'B3',
            _RED_KEY: 'B4',
            _NIR_KEY: 'B5',
            _SWIR_1_KEY: 'B6',
            _SWIR_2_KEY: 'B7',
            _BRIGHTNESS_TEMPERATURE_1_KEY: 'B10',
            _BRIGHTNESS_TEMPERATURE_2_KEY: 'B11'
        }
    }, GSV_DS_LANDSAT_8_TOA_T1_KEY: {  # LANDSAT 8 SR TOA
        _COLLECTION_ID_KEY: 'LANDSAT/LC08/C01/T1_TOA',
        _DATE_KEY: {
            _START_DATE_KEY: '1999-01-01T00:00:00',
            _END_DATE_KEY: '2021-01-15T00:00:00'
        },
        _BANDS_KEY: {
            _COASTAL_AEROSOL_KEY: 'B1',
            _BLUE_KEY: 'B2',
            _GREEN_KEY: 'B3',
            _RED_KEY: 'B4',
            _NIR_KEY: 'B5',
            _SWIR_1_KEY: 'B6',
            _SWIR_2_KEY: 'B7',
            _PANCHROMATIC_KEY: 'B8',
            _CIRRUS_KEY: 'B9',
            _THERMAL_INFRARED_1_KEY: 'B10',
            _THERMAL_INFRARED_2_KEY: 'B11',
            _BQA_KEY: 'BQA'
        }
    }, GSV_DS_LANDSAT_8_RAW_T1_KEY: {  # LANDSAT 8 RAW
        _COLLECTION_ID_KEY: 'LANDSAT/LC08/C01/T1',
        _DATE_KEY: {
            _START_DATE_KEY: '2013-04-11T00:00:00',
            _END_DATE_KEY: '2021-02-05T00:00:00'
        },
        _BANDS_KEY: {
            _COASTAL_AEROSOL_KEY: 'B1',
            _BLUE_KEY: 'B2',
            _GREEN_KEY: 'B3',
            _RED_KEY: 'B4',
            _NIR_KEY: 'B5',
            _SWIR_1_KEY: 'B6',
            _SWIR_2_KEY: 'B7',
            _PANCHROMATIC_KEY: 'B8',
            _CIRRUS_KEY: 'B9',
            _THERMAL_INFRARED_1_KEY: 'B10',
            _THERMAL_INFRARED_2_KEY: 'B11',
            _BQA_KEY: 'BQA'
        }
    }, GSV_DS_LANDSAT_8_8DAY_BAI_KEY: {  # LANDSAT 8 BAI
        _COLLECTION_ID_KEY: 'LANDSAT/LC08/C01/T1_8DAY_BAI',
        _DATE_KEY: {
            _START_DATE_KEY: '2017-01-01',
            _END_DATE_KEY: '2017-12-31'
        },
        _BANDS_KEY: {
            _SINGLE_BAND_KEY: 'BAI'
        }
    }, GSV_DS_LANDSAT_8_8DAY_EVI_KEY: {  # LANDSAT 8 EVI
        _COLLECTION_ID_KEY: 'LANDSAT/LC08/C01/T1_8DAY_EVI',
        _DATE_KEY: {
            _START_DATE_KEY: '2017-01-01',
            _END_DATE_KEY: '2017-12-31'
        },
        _BANDS_KEY: {
            _SINGLE_BAND_KEY: 'EVI'
        }
    }, GSV_DS_LANDSAT_8_8DAY_NDVI_KEY: {  # LANDSAT 8 NDVI
        _COLLECTION_ID_KEY: 'LANDSAT/LC08/C01/T1_8DAY_NDVI',
        _DATE_KEY: {
            _START_DATE_KEY: '2017-01-01',
            _END_DATE_KEY: '2017-12-31'
        },
        _BANDS_KEY: {
            _SINGLE_BAND_KEY: 'NDVI'
        }
    }, GSV_DS_LANDSAT_8_8DAY_NBRT_KEY: {  # LANDSAT 8 NBRT
        _COLLECTION_ID_KEY: 'LANDSAT/LC08/C01/T1_8DAY_NBRT',
        _DATE_KEY: {
            _START_DATE_KEY: '2017-01-01',
            _END_DATE_KEY: '2017-12-31'
        },
        _BANDS_KEY: {
            _SINGLE_BAND_KEY: 'NBRT'
        }
    }, GSV_DS_LANDSAT_8_8DAY_NDSI_KEY: {  # LANDSAT 8 NDSI
        _COLLECTION_ID_KEY: 'LANDSAT/LC08/C01/T1_8DAY_NDSI',
        _DATE_KEY: {
            _START_DATE_KEY: '2017-01-01',
            _END_DATE_KEY: '2017-12-31'
        },
        _BANDS_KEY: {
            _SINGLE_BAND_KEY: 'NDSI'
        }
    }, GSV_DS_LANDSAT_8_8DAY_NDWI_KEY: {  # LANDSAT 8 NDWI
        _COLLECTION_ID_KEY: 'LANDSAT/LC08/C01/T1_8DAY_NDWI',
        _DATE_KEY: {
            _START_DATE_KEY: '2017-01-01',
            _END_DATE_KEY: '2017-12-31'
        },
        _BANDS_KEY: {
            _SINGLE_BAND_KEY: 'NDWI'
        }
    }, GSV_DS_SENTINEL_1_SAR_GRD_KEY: {  # SENTINEL 1 SAR GRD
        _COLLECTION_ID_KEY: 'COPERNICUS/S1_GRD',
        _DATE_KEY: {
            _START_DATE_KEY: '2014-10-03T00:00:00',
            _END_DATE_KEY: '2021-02-10T00:00:00'
        },
        _BANDS_KEY: {
            _HH_KEY: 'HH',
            _HV_KEY: 'HV',
            _VV_KEY: 'VV',
            _VH_KEY: 'VH',
        }
    },
}


# -------------------------------------------------- #
# ---------- 3. Create Internal Functions ---------- #
# -------------------------------------------------- #

# ----------------------------------------- #
# ---------- 4. Create Functions ---------- #
# ----------------------------------------- #

def prt_dict_full_data():
    print(DICT_FULL_DATASET)


def prt_dict_full_dataset(dataset_id):
    if dataset_id in DICT_FULL_DATASET.keys():
        print(DICT_FULL_DATASET[dataset_id])
    else:
        print("<" + dataset_id + "> dataset does not exist in dictionary.")


def get_default_date_range_from_dict_dataset(dataset_id):
    return [DICT_FULL_DATASET[dataset_id][_DATE_KEY][_START_DATE_KEY],
            DICT_FULL_DATASET[dataset_id][_DATE_KEY][_END_DATE_KEY]]


# ------------------------------ #
# ---------- 5. Class ---------- #
# ------------------------------ #


class GoogleEarthEngine:
    """
    This Class will be the core routine
    """

    def __init__(self):
        self._image_collection = None
        self._collection_date_range = None
        self._collection_bounds_geometry = None
        self._image = None
        self._dataset_id = None
        self._export_name = ""

    # ----- Print Functions (Debugging) ----- #

    def prt_image_collection(self):
        print(self._image_collection)

    def prt_date_range(self):
        print(self._collection_date_range)

    def prt_image_geometry(self):
        print(self._collection_bounds_geometry)

    def prt_image(self):
        print(self._image)

    # ----- Core Functions ----- #

    def set_collection_date_range(self, date_range: []):
        self._collection_date_range = date_range

    def set_collection_geometry_from_gee_country_str(self, country: str):
        # Simple create a geometry from GEE country list
        self._collection_bounds_geometry = _GEOMETRY_COUNTRY_COLLECTION.filter(ee.Filter.eq('Country', country))
        self._collection_bounds_geometry = self._collection_bounds_geometry.geometry()

    def set_collection_geometry_from_gee_country_list(self, list_country: []):
        new_geometry = None  # Create a temporary tmp geometry

        for index in range(0, len(list_country)):
            if index == 0:
                new_geometry = _GEOMETRY_COUNTRY_COLLECTION.filter(ee.Filter.eq('Country', list_country[index]))
                new_geometry = new_geometry
            else:
                tmp_geometry = _GEOMETRY_COUNTRY_COLLECTION.filter(ee.Filter.eq('Country', list_country[index]))
                tmp_geometry = tmp_geometry
                new_geometry.merge(tmp_geometry)

        self._collection_bounds_geometry = new_geometry.geometry()

    def set_collection(self, dataset_id):
        """
        Set the ee.ImageCollection(), which will be used for processing
        :param dataset_id: the DICT_FULL_DATASET key
        :return: Nothing
        """
        if dataset_id in DICT_FULL_DATASET.keys():  # if dataset_id in DICT_FULL_DATASET key list
            self._export_name += DICT_FULL_DATASET[dataset_id][_COLLECTION_ID_KEY].replace("/", "_")
            self._dataset_id = dataset_id
            # Set the _image_collection
            self._image_collection = ee.ImageCollection(DICT_FULL_DATASET[dataset_id][_COLLECTION_ID_KEY])
            # print(self._image_collection, '\n')
            if self._collection_date_range is not None:  # Check if date range is not none
                # If True, then filter by the date range
                self._image_collection = self._image_collection.filterDate(self._collection_date_range[0],
                                                                           self._collection_date_range[0])
                self._export_name += "_" + self._collection_date_range[0].replace("-", "") + \
                                     self._collection_date_range[0].replace("-", "")
                # print(self._image_collection, '\n')
            if self._collection_bounds_geometry is not None:  # Check if geometry is not none
                # If True, then filter by geometry
                self._image_collection = self._image_collection.filterBounds(self._collection_bounds_geometry)
                # print(self._image_collection, '\n')
        else:  # if dataset_id not in FICT_FULL_DATASET key list
            print("Error: Uknown Dataset.")  # print error

    def create_image_index(self, index_name, clip_image=False):
        if index_name == BAI_INDEX:
            tmp_mean_img = self._image_collection.mean()
            self._image = tmp_mean_img.expression(
                '1.0 / ((0.1 - RED)**2 + (0.06 - NIR)**2)',
                {
                    'RED': tmp_mean_img.select(DICT_FULL_DATASET[self._dataset_id][_BANDS_KEY][_RED_KEY]),
                    'NIR': tmp_mean_img.select(DICT_FULL_DATASET[self._dataset_id][_BANDS_KEY][_NIR_KEY])
                }
            )
            self._export_name += '_BAI'
        elif index_name == EVI_INDEX:
            pass
        elif index_name == NDVI_INDEX:
            tmp_mean_img = self._image_collection.mean()
            self._image = tmp_mean_img.expression(
                '(NIR - RED) / (NIR + RED)',
                {
                    'RED': tmp_mean_img.select(DICT_FULL_DATASET[self._dataset_id][_BANDS_KEY][_RED_KEY]),
                    'NIR': tmp_mean_img.select(DICT_FULL_DATASET[self._dataset_id][_BANDS_KEY][_NIR_KEY])
                }
            )
            self._export_name += '_NDVI'
        elif index_name == NBRT_INDEX:
            pass
        elif index_name == NDSI_INDEX:
            pass
        elif index_name == NDWI_INDEX:
            pass
        else:
            print("Error: Uknown Index")
            return
        if clip_image:
            if self._collection_bounds_geometry is not None:
                self._image = self._image.clip(self._collection_bounds_geometry)

    def export_to_drive(self, export_name=None, scale_m2_px=1000):
        description = self._export_name
        if export_name is not None:
            description = export_name
        task_bash = {
            'image': self._image,
            'description': description,
            'region': self._collection_bounds_geometry,
            'scale': scale_m2_px,
            'folder': 'GEE_TEST'
        }
        task = ee.batch.Export.image.toDrive(**task_bash)
        task.start()
