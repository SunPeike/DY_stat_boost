import CRABClient
from CRABClient.UserUtilities import config 

config = config()

config.General.requestName = 'HtoZg_DY_fakePhoton_2024_E_mini_el_ph_removal_v3'
config.General.workArea = 'crab_projects_el_ph_removal'
config.General.transferOutputs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'ConfigDY2024.py'


#config.Data.inputDataset = '/DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM'
config.Data.inputDataset = '/DYto2E-2Jets_Bin-MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v4/MINIAODSIM'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 50
#config.Data.totalUnits = 10

config.Data.allowNonValidInputDataset = True
config.Data.publication = False
config.Data.outputDatasetTag = 'HtoZg_DY_fakePhoton_2024_E_mini'
#config.Data.outputPrimaryDataset = 'test'
config.Site.storageSite = 'T3_CH_CERNBOX'
