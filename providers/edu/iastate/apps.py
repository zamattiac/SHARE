from share.provider import OAIProviderAppConfig


class AppConfig(OAIProviderAppConfig):
    name = 'providers.edu.iastate'
    version = '0.0.1'
    title = 'iastate'
    long_title = 'Digital Repository @ Iowa State University'
    home_page = 'http://lib.dr.iastate.edu'
    url = 'http://lib.dr.iastate.edu/do/oai/'
    approved_sets = [
        'museums_rediscoveringshelves',
        'museums_rediscoveringshelves_installation',
        'museums_rediscoveringshelves_videos',
        'extension_4h',
        'extension_4h_pubs',
        'abe_carousel',
        'acct',
        'acct_pubs',
        'accounting_pubs',
        'admin',
        'abe_eng_advancedmachinery',
        'abe_ag_advancedmachinery',
        'abe_ag_advancedmachinery_conf',
        'abe_eng_advancedmachinery_conf',
        'abe_ag_advancedmachinery_pubs',
        'abe_eng_advancedmachinery_pubs',
        'cbe_advancedmaterials',
        'cbe_advancedmaterials_conf',
        'cbe_advancedmaterials_pubs',
        'aere',
        'aere_conf',
        'aere_patents',
        'aere_pubs',
        'aere_etd',
        'afam',
        'afam_pubs',
        'agdm',
        'farms_centraliowa_reports',
        'ageds',
        'ageds_etd',
        'safefarm_ag',
        'safefarm',
        'safefarm_ag_pubs',
        'safefarm_pubs',
        'agpolicyreview',
        'ag_researchbulletins',
        'abe_ag',
        'abe_eng',
        'abe_eng_books',
        'abe_ag_books',
        'abe_eng_conf',
        'abe_ag_extensionpubs',
        'abe_eng_extensionpubs',
        'abe_eng_patents',
        'abe_ag_patents',
        'abe_ag_conf',
        'abe_ag_reports',
        'abe_eng_pubs',
        'abe_ag_pubs',
        'abe_eng_researchareas',
        'abe_eng_reports',
        'abe_ag_etd',
        'abe_eng_etd',
        'extension_ag_pubs',
        'extension_ag',
        'agron',
        'agron_conf',
        'agron_pubs',
        'agron_reports',
        'agron_etd',
        'airforce',
        'airforce_pubs',
        'a2ru',
        'amin',
        'amin_pubs',
        'ameslab',
        'ameslab_manuscripts',
        'ameslab_conf',
        'ameslab_iscreports',
        'ameslab_patents',
        'ameslab_pubs',
        'ameslab_software',
        'ameslab_isreports',
        'aecl',
        'aecl_pubs',
        'aecl_etd',
        'ans_air',
        'abe_eng_animalproduction',
        'abe_ag_animalproduction',
        'abe_eng_animalproduction_conf',
        'abe_ag_animalproduction_conf',
        'abe_eng_animalproduction_pubs',
        'abe_ag_animalproduction_pubs',
        'ans',
        'ans_conf',
        'ans_pubs',
        'ans_reports',
        'ans_etd',
        'ans_whitepapers',
        'anthr',
        'anthr_pubs',
        'anthr_etd',
        'aeshm',
        'aeshm_conf',
        'aeshm_pubs',
        'aeshm_etd',
        'arch',
        'arch_books',
        'arch_conf',
        'arch_announcements',
        'arch_pubs',
        'arch_etd',
        'farms_armstrong_reports',
        'ad',
        'ad_conf',
        'ad_etd',
        'avc',
        'avc_creativeworks',
        'avc_pubs',
        'asam',
        'asam_pubs',
        'baltic_reports',
        'balticbasin_reports',
        'beefreports_1996',
        'beefreports_1997',
        'beefreports_1998',
        'beefreports_1999',
        'beefreports_2000',
        'beefreports_2001',
        'beefreports_2002',
        'beefreports_2003',
        'bce_proceedings',
        'bbmb_ag',
        'bbmb_las',
        'bbmb_ag_pubs',
        'bbmb_las_etd',
        'bbmb_ag_etd',
        'bbmb_ag_conf',
        'bei',
        'bei_reports',
        'bcb_etd',
        'abe_ag_biologicalprocess',
        'abe_eng_biologicalprocess',
        'abe_ag_biologicalprocess_conf',
        'abe_eng_biologicalprocess_conf',
        'abe_ag_biologicalprocess_pubs',
        'abe_eng_biologicalprocess_pubs',
        'bms',
        'bms_pubs',
        'bms_reports',
        'bms_etd',
        'brt_etd',
        'cbe_biorenewables',
        'cbe_biorenewables_conf',
        'cbe_biorenewables_pubs',
        'bot',
        'botany_etd',
        'bot_pubs',
        'bot_etd',
        'experimentstation_bulletin',
        'business_etd',
        'card_books',
        'card_briefingpapers',
        'card_pubs',
        'card_policybriefs',
        'card_pres',
        'card_reports',
        'card_publications',
        'card_staffreports',
        'card_technicalreports',
        'card_workingpapers',
        'carver',
        'carver_narratives',
        'cbe_catalysis',
        'cbe_catalysis_conf',
        'cbe_catalysis_pubs',
        'card',
        'cbirc_annualreports',
        'ccur',
        'ccur_conf',
        'ccur_pubs',
        'cfsph',
        'cfsph_pubs',
        'cnde',
        'cnde_conf',
        'cnde_reports',
        'cnde_pubs',
        'cnde_etd',
        'edesign',
        'edesign_newsletters',
        'edesign_conf',
        'edesign_pubs',
        'edesign_etd',
        'cbe',
        'cbe_conf',
        'cbe_pubs',
        'cbe_researchareas',
        'cbe_etd',
        'chem',
        'chem_conf',
        'chem_pubs',
        'chem_etd',
        'libaccess',
        'libaccess_conf',
        'libaccess_workshops',
        'libaccess_pubs',
        'ccee',
        'ccee_books',
        'ccee_conf',
        'ccee_pubs',
        'ccee_researchareas',
        'ccee_etd',
        'libcat',
        'libcat_conf',
        'libcat_pubs',
        'ag',
        'business',
        'design',
        'colledu',
        'engineering',
        'hs',
        'chsmatters',
        'las',
        'vetmed',
        'communitymatters',
        'communityplanning',
        'communityplanning_pubs',
        'communityplanning_etd',
        'cbe_fluiddynamics',
        'cbe_fluiddynamics_conf',
        'cbe_fluiddynamics_pubs',
        'cs_techreports_applications',
        'cs',
        'cs_pubs',
        'cs_techreports',
        'cs_etd',
        'cs_techreports_compsystems',
        'cs_techreports_methodologies',
        'cs_techreports_milleux',
        'pres_portfolio',
        'ccee_construction',
        'ccee_construction_conf',
        'ccee_construction_pubs',
        'cornbeltcowcalf',
        'ci',
        'ci_etd',
        'ci_pubs',
        'dae-card_sectoranalysis',
        'ebooks',
        'cs_techreports_data',
        'entnewsletter',
        'housing',
        'housing_books',
        'digirep',
        'digirep_conf',
        'digirep_outreach',
        'digirep_pubs',
        'dimensions',
        'dgtc_symposium',
        'diversityreports',
        'driftlessconference',
        'eeb_etd',
        'eeob_las',
        'eeob_ag',
        'eeob_conf',
        'eeob_ag_pubs',
        'eeob_las_pubs',
        'eeob_ag_reports',
        'eeob_las_etd',
        'eeob_ag_etd',
        'econ_las_staffpapers',
        'econ_ag_staffpapers',
        'econ_ag',
        'econ_las',
        'econ_ag_conf',
        'econ_las_conf',
        'econ_las_pubs',
        'econ_ag_etd',
        'econ_las_etd',
        'edu_pubs',
        'elps',
        'elps_pubs',
        'elps_etd',
        'ece',
        'ece_books',
        'ece_conf',
        'ece_pubs',
        'ece_reports',
        'ece_etd',
        'engl',
        'engl_books',
        'engl_conf',
        'engl_pubs',
        'engl_etd',
        'ent',
        'ent_conf',
        'ent_pubs',
        'ent_reports',
        'ent_etd',
        'ensci_etd',
        'ensci_studentprojects',
        'ccee_environmental',
        'ccee_environmental_conf',
        'ccee_environmental_pubs',
        'ethos',
        'extension_communities',
        'extension_communities_pubs',
        'extension',
        'hs_extension_conf',
        'extension_conf',
        'extension_pubs',
        'extension_research',
        'hs_extension',
        'hs_extension_pubs',
        'fapri_staffreports',
        'ir_factbooks',
        'finance',
        'finance_pubs',
        'fshn_ag',
        'fshn_hs',
        'fshn_ag_extensionpubs',
        'fshn_hs_extensionpubs',
        'fshn_ag_patents',
        'fshn_hs_patents',
        'fshn_hs_conf',
        'fshn_ag_conf',
        'fshn_ag_pubs',
        'fshn_hs_pubs',
        'fshn_ag_etd',
        'fshn_hs_etd',
        'for',
        'for_pubs',
        'for_reports',
        'for_etd',
        'gatt_papers',
        'cs_techreports_general',
        'genetics_etd',
        'gdcb_conf',
        'gdcb_ag',
        'gdcb_las',
        'gdcb_las_pubs',
        'gdcb_ag_etd',
        'gdcb_las_etd',
        'gentle_doctor',
        'ge_at',
        'ge_at_etd',
        'ge_at_pubs',
        'ccee_geotechnical',
        'ccee_geotechnical_conf',
        'ccee_geotechnical_pubs',
        'gerontology_etd',
        'grad',
        'grad_reports',
        'etd',
        'graphicdesign',
        'graphicdesign_etd',
        'jlmc',
        'cs_techreports_hardware',
        'cbe_biomedical',
        'cbe_biomedical_conf',
        'cbe_biomedical_pubs',
        'ag_hist',
        'design_hist',
        'las_hist',
        'hs_hist',
        'history',
        'history_books',
        'history_conf',
        'history_pubs',
        'history_etd',
        'honors_posters',
        'hort',
        'hort_conf',
        'hort_pubs',
        'farms_horticulture_reports',
        'hort_etd',
        'hci_etd',
        'hdfs',
        'hdfs_extensionpubs',
        'hdfs_conf',
        'hdfs_pubs',
        'hdfs_reports',
        'hdfs_etd',
        'extension_families',
        'extension_families_pubs',
        'imsenews',
        'econ_las_economicreports',
        'econ_ag_economicreports',
        'immunobiology_etd',
        'intrans_reports',
        'industrialdesign',
        'industrialdesign_etd',
        'iet_pubs',
        'iet',
        'imse',
        'imse_conf',
        'imse_pubs',
        'imse_reports',
        'imse_etd',
        'infas_etd',
        'cs_techreports_infosystems',
        'is_etd',
        'inspire',
        'iprt',
        'intrans',
        'ir',
        'cropnews',
        'interdisciplinaryprograms_graduate',
        'cnde_yellowjackets',
        'grad_etd',
        'id',
        'id_conf',
        'id_etd',
        'safepork',
        'iowaagreview',
        'iaes_circulars',
        'iahees',
        'ibc',
        'cfwru',
        'cfwru_reports',
        'ipic',
        'ipic_factsheets',
        'ipic_handbooks',
        'iowastatedaily',
        'iowastatedaily_2010',
        'iowastatedaily_2011',
        'iowastatedaily_2012',
        'iowastatedaily_2013',
        'iowastatedaily_2014',
        'iowastatedaily_2015',
        'iowastatedaily_2011-04',
        'iowastatedaily_2012-04',
        'iowastatedaily_2013-04',
        'iowastatedaily_2014-04',
        'iowastatedaily_2015-04',
        'iowastatedaily_2010-08',
        'iowastatedaily_2011-08',
        'iowastatedaily_2012-08',
        'iowastatedaily_2013-08',
        'iowastatedaily_2014-08',
        'iowastatedaily_2015-08',
        'iowastatedaily_2010-12',
        'iowastatedaily_2011-12',
        'iowastatedaily_2012-12',
        'iowastatedaily_2013-12',
        'iowastatedaily_2014-12',
        'iowastatedaily_2015-12',
        'iowastatedaily_2011-02',
        'iowastatedaily_2012-02',
        'iowastatedaily_2013-02',
        'iowastatedaily_2014-02',
        'iowastatedaily_2015-02',
        'iowastatedaily_2011-01',
        'iowastatedaily_2012-01',
        'iowastatedaily_2013-01',
        'iowastatedaily_2014-01',
        'iowastatedaily_2015-01',
        'iowastatedaily_2010-07',
        'iowastatedaily_2011-07',
        'iowastatedaily_2012-07',
        'iowastatedaily_2013-07',
        'iowastatedaily_2014-07',
        'iowastatedaily_2015-07',
        'iowastatedaily_2010-06',
        'iowastatedaily_2011-06',
        'iowastatedaily_2012-06',
        'iowastatedaily_2013-06',
        'iowastatedaily_2014-06',
        'iowastatedaily_2015-06',
        'iowastatedaily_2011-03',
        'iowastatedaily_2012-03',
        'iowastatedaily_2013-03',
        'iowastatedaily_2014-03',
        'iowastatedaily_2015-03',
        'iowastatedaily_2010-05',
        'iowastatedaily_2011-05',
        'iowastatedaily_2012-05',
        'iowastatedaily_2013-05',
        'iowastatedaily_2014-05',
        'iowastatedaily_2015-05',
        'iowastatedaily_2010-11',
        'iowastatedaily_2011-11',
        'iowastatedaily_2012-11',
        'iowastatedaily_2013-11',
        'iowastatedaily_2014-11',
        'iowastatedaily_2015-11',
        'iowastatedaily_2010-10',
        'iowastatedaily_2011-10',
        'iowastatedaily_2012-10',
        'iowastatedaily_2013-10',
        'iowastatedaily_2014-10',
        'iowastatedaily_2015-10',
        'iowastatedaily_2010-09',
        'iowastatedaily_2011-09',
        'iowastatedaily_2012-09',
        'iowastatedaily_2013-09',
        'iowastatedaily_2014-09',
        'iowastatedaily_2015-09',
        'farms_reports',
        'farms_reportsbyfarm',
        'catalog',
        'patents',
        'isurf',
        'farms',
        'iowastate_veterinarian',
        'weedbiology',
        'icip',
        'jctp',
        'jlmc_etd',
        'jlmc_pubs',
        'kin',
        'kin_pubs',
        'kin_etd',
        'abe_eng_landwaterresources',
        'abe_ag_landwaterresources',
        'abe_ag_landwaterresources_conf',
        'abe_eng_landwaterresources_conf',
        'abe_eng_landwaterresources_pubs',
        'abe_ag_landwaterresources_pubs',
        'landscapearchitecture',
        'landscapearchitecture_conf',
        'landscapearchitecture_pubs',
        'landscapearchitecture_etd',
        'lau_slideshow',
        'leadership',
        'leadership_conf',
        'leadership_pubs',
        'leopold_annualreports',
        'leopold_grantreports',
        'leopold_extension',
        'leopold_proceedings',
        'leopold_pubspapers',
        'leopold',
        'leopold_letter',
        'libadmin',
        'libadmin_conf',
        'libadmin_pubs',
        'library_books',
        'libit_pubs',
        'libreports',
        'livestock',
        'matric_briefingpapers',
        'matric_researchpapers',
        'matric_workingpapers',
        'management',
        'management_pubs',
        'management_reports',
        'marketing_pubs',
        'mse',
        'mse_conf',
        'mse_pubs',
        'mse_etd',
        'math',
        'math_conf',
        'math_etd',
        'cs_techreports_mathematics',
        'math_pubs',
        'farms_mcnay_reports',
        'meatscience',
        'meatscience_air',
        'meatscience_pubs',
        'me',
        'me_conf',
        'me_pubs',
        'me_etd',
        'me_whitepapers',
        'im_etd',
        'micro',
        'micro_pubs',
        'micro_etd',
        'armyrotc',
        'armyrotc_pubs',
        'mcdb_etd',
        'farms_muscatine_reports',
        'music_pubs',
        'music_recordings',
        'music',
        'ncrac_annualreports',
        'ncrac_cultureguides',
        'ncrac_factsheets',
        'ncrac_techbulletins',
        'ncrac_whitepapers',
        'ncrpis_conf',
        'ncrpis_pubs',
        'cbirc',
        'swinefeedefficiency',
        'nrem',
        'nrem_conf',
        'nrem_extensionpubs',
        'nrem_pubs',
        'nrem_studentprojects',
        'nrem_etd',
        'nrem_reports',
        'navy',
        'navy_pubs',
        'resilientneighborhoods_plans',
        'neuroscience_etd',
        'ncrac',
        'ncrac_pubs',
        'ncrac_etd',
        'ncrac_conferences',
        'ncrpis',
        'farms_northeast_reports',
        'farms_northern_reports',
        'farms_northwest_reports',
        'igpns_etd',
        'abe_eng_occupationalsafety',
        'abe_ag_occupationalsafety',
        'abe_ag_occupationalsafety_conf',
        'abe_eng_occupationalsafety_conf',
        'abe_ag_occupationalsafety_pubs',
        'abe_eng_occupationalsafety_pubs',
        'provost_reports',
        'registrar',
        'provost',
        'philrs',
        'philrs_pubs',
        'physastro',
        'physastro_conf',
        'physastro_pubs',
        'physastro_etd',
        'ipb_etd',
        'plantpath_conf',
        'plantpath',
        'plantpath_pubs',
        'plantpath_etd',
        'pols',
        'pols_pubs',
        'pols_etd',
        'icip_poverty',
        'pres',
        'pres_conf',
        'pres_workshops',
        'pres_pubs',
        'cnde_yellowjackets_1976',
        'cnde_yellowjackets_1978',
        'cnde_yellowjackets_1977',
        'cnde_yellowjackets_1975',
        'cnde_yellowjackets_1979',
        'cnde_yellowjackets_1981',
        'cnde_yellowjackets_1974',
        'psychology',
        'psychology_conf',
        'psychology_pubs',
        'psychology_etd',
        'refinst',
        'refinst_conf',
        'refinst_pubs',
        'cbe_renewableenergy',
        'cbe_renewableenergy_conf',
        'cbe_renewableenergy_pubs',
        'ccee_reports',
        'abe_ag_researchareas',
        'resilientneighborhoods',
        'resilientneighborhoods_memos',
        'resilientneighborhoods_reports',
        'rtd',
        'qnde',
        'revival',
        'stories',
        'safefarm_ag_extension',
        'safefarm_extension',
        'safefarmminute_ag',
        'safefarmminute',
        'safefarm_minutes',
        'safepork_covers',
        'edu',
        's2erc',
        's2erc_reports',
        'stb_etd',
        'sheepreports_1997',
        'sketch',
        'soc_las',
        'soc_ag',
        'soc_las_extensionpubs',
        'soc_las_pubs',
        'soc_las_reports',
        'soc_las_etd',
        'soc_ag_etd',
        'cs_techreports_software',
        'farms_southeast_reports',
        'soybeanaphid_podcasts',
        'speccoll_conf',
        'speccoll_exhibits',
        'speccoll_outreach',
        'speccoll_pubs',
        'speccoll',
        'stat_las',
        'stat_ag',
        'stat_ag_conf',
        'stat_las_conf',
        'stat_las_preprints',
        'stat_ag_preprints',
        'stat_las_pubs',
        'stat_las_etd',
        'stat_ag_etd',
        'stories_covers',
        'ccee_structural',
        'ccee_structural_conf',
        'ccee_structural_pubs',
        'scm_conf',
        'scm',
        'scm_pubs',
        'susag_conf',
        'susag',
        'susag_pubs',
        'gpsa_etd',
        'swinefeedefficiency_air',
        'swinefeedefficiency_conf',
        'swinefeedefficiency_factsheets',
        'swinefeedefficiency_pubs',
        'swinefeedefficiency_etd',
        'swinereports_1996',
        'swinereports_1997',
        'swinereports_1998',
        'swinereports_1999',
        'swinereports_2000',
        'swinereports_2001',
        'swinereports_2002',
        'undergradresearch_symposium',
        'systemseng_etd',
        'intrans_techtransfer',
        'cs_techreports_subjects',
        'tcmuseum',
        'tcmuseum_exhibits',
        'tcmuseum_installation',
        'cs_techreports_theory',
        'toxicology_etd',
        'trans_etd',
        'ccee_transportation',
        'ccee_transportation_conf',
        'ccee_transportation_pubs',
        'trend',
        'usls',
        'usls_pubs',
        'uhuru',
        'undergradresearch',
        'honors',
        'library',
        'bookmarks',
        'museums',
        'museums_exhibitguides',
        'museums_exhibits',
        'museums_installation',
        'museums_videos',
        'vcs',
        'vcs_conf',
        'vcs_pubs',
        'vcs_reports',
        'vcs_etd',
        'vdpam',
        'vdpam_conf',
        'vdpam_pubs',
        'vdpam_reports',
        'vdpam_etd',
        'vmpm',
        'vmpm_pubs',
        'vmpm_reports',
        'vmpm_etd',
        'vpath',
        'vpath_conf',
        'vpath_pubs',
        'vpath_reports',
        'vpath_etd',
        'vrac',
        'vrac_conf',
        'vrac_pubs',
        'weedscience_reports',
        'farms_western_reports',
        'withhonors',
        'tcmuseum_exhibits_womenforwomen',
        'language',
        'language_conf',
        'language_pubs',
        'zool',
        'zool_pubs',
        'zool_etd',
        'a2ru_photos',
    ]
