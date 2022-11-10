#scraping library
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

class arrayLinks:
            cF = "تغییر فایل"
            notCF = "عدم تغییر فایل"
            fA = "آدرس درختی فایل در سایت سفارت آلمان👇"
            
            def arrayLinksFunc(self):
                    objFV_1 = CurrentContainerClass().schulerVisum()  
                    objFNV_2 = CurrentContainerClass().nemuneVekalat()
                    objChLSch_3 = CurrentContainerClass().checkListSchengen()
                    objMSchDB_4 = CurrentContainerClass().madarekSchengenDidarBastegan()
                    objMSchN_5 = CurrentContainerClass().madarekSchengenNamaeshgah()
                    objMSchT_6 = CurrentContainerClass().madarekSchengenTejari()
                    objMSchMK_7 = CurrentContainerClass().madarekSchengenMamurKari()
                    objMSchCS_8 = CurrentContainerClass().madarekSchengenCongressSeminar()
                    objMSchMV_9 = CurrentContainerClass().madarekSchengenMosabeghVarzeshi()
                    objMSchT_10 = CurrentContainerClass().madarekSchengenTransit()
                    objMSchD_11 = CurrentContainerClass().madarekSchengenDarman()
                    objMSchHB_12 =CurrentContainerClass().madarekSchengenHamrahiBimar()
                    objPPS_13 = CurrentContainerClass().photoPassSample()
                    objERV_14 = CurrentContainerClass().explanationRejectVisa()
                    objFVN_15 = CurrentContainerClass().formVekalatNameh()
                    objFDV_16 = CurrentContainerClass().formDarkhastVisa()
                    objRDVK_17 = CurrentContainerClass().rahnamaDarkhastVisaKar()
                    objRDVTSh_18 = CurrentContainerClass().rahnamaDarkhastVisaTasisSherkat()
                    objRDVE_19 = CurrentContainerClass().rahnamaDarkhastVisaEzdevaj()
                    objRDJK_20 = CurrentContainerClass().rahnamaDarkhastJostejuyeKar()
                    objRDVM_21 = CurrentContainerClass().rahnamaDarkhastVorudMojadad()
                    objRDVDD_22 = CurrentContainerClass().rahnamaDarkhastVisaDaneshjooDoctora()
                    objRDDMP_23 = CurrentContainerClass().rahnamaDarkhastDaneshmandanMihmanPajooheshgaran()
                    objRDATMVPA_24 = CurrentContainerClass().rahnamaDarkhastArzeshyabiTaidMadarekVaParvanehKharejAlman()
                    objRDVPKhH_25 = CurrentContainerClass().rahnamaDarkhastVisaPeywastKhanevadehHamsar()
                    objRDVPFBPYM_26 = CurrentContainerClass().rahnamaDarkhastVisaPeywastFarzandBePedarYaMadar()
                    objRDVPVBF_27 = CurrentContainerClass().rahnamaDarkhastVisaPeywastValedeinBeFarzand()
                    objRDVPBKhA_28 = CurrentContainerClass().rahnamaDarkhastVisaPeywastBeKhanevadehAfghanha()
                    objRDVBAA_29 = CurrentContainerClass().rahnamaDarkhastVisaBaresiAsnadAfghani()
                    objHBVAI_30 = CurrentContainerClass().hazinehBarresiVisaAtbaIrani()
                    objEMHVBKD_31 = CurrentContainerClass().etelatMafiatHazinehayeVisaBarayeKeshvarhayeDigar()
                    objVTG_32 = CurrentContainerClass().vekalatnameTahvilGozarnameh()
                    objEHVBKDF_33 = CurrentContainerClass().etelatMafiatHazinehayeVisaBarayeKeshvarhayeDigarFarsi()
                    # objZEEVSBHG_34 = CurrentContainerClass().zamanEhtemaliEntezarVaghtSefaratBarayeHarGrouh()
                    objRTM_35 = CurrentContainerClass().rahnameTaidMadarek()
                    objTCMkD_36 = CurrentContainerClass().taidCopyMadrakDaneshjoo()
                    objEAE_37 = CurrentContainerClass().enserafAzErs()
                    objEAEBK_38 = CurrentContainerClass().enserafAzErsBarayeKoodakan()
                    objFDGASP_39 = CurrentContainerClass().formDarkhastGovahiAdamSuePishineh()
                    objFDGASPE_40 = CurrentContainerClass().formDarkhastGovahiAdamSuePishinehEnglish()
                    objVSHU_41 = CurrentContainerClass().vorudSafarHeywanatUropa()
                    objMSchT_42 = CurrentContainerClass().madarekSchengenTursist()
                    # objpMRM_1_43 = CurrentContainerClass().pasokhMosbatRavadidhayeMelli_1()
                    # objpMRM_2_44 = CurrentContainerClass().pasokhMosbatRavadidhayeMelli_2() 
                    linksArray = [objFV_1,objFNV_2,objChLSch_3,objMSchDB_4,objMSchN_5,objMSchT_6,objMSchMK_7,objMSchCS_8,objMSchMV_9,objMSchT_10,objMSchD_11,objMSchHB_12,objPPS_13,objERV_14,objFVN_15,objFDV_16,objRDVK_17,objRDVTSh_18,objRDVE_19,objRDJK_20,objRDVM_21,objRDVDD_22,objRDDMP_23,objRDATMVPA_24,objRDVPKhH_25,objRDVPFBPYM_26,objRDVPVBF_27,objRDVPBKhA_28,objRDVBAA_29,objHBVAI_30,objEMHVBKD_31,objVTG_32,objEHVBKDF_33,objRTM_35,objTCMkD_36,objEAE_37,objEAEBK_38,objFDGASP_39,objFDGASPE_40,objVSHU_41,objMSchT_42]
                    #objZEEVSBHG_34
                    # linksArray = [objFV_1,objFNV_2,objChLSch_3,objMSchDB_4,objMSchN_5,objMSchT_6,objMSchMK_7,objMSchCS_8,objMSchMV_9,objMSchT_10,objMSchD_11,objMSchHB_12,objPPS_13,objERV_14,objFVN_15,objFDV_16,objRDVK_17,objRDVTSh_18,objRDVE_19,objRDJK_20,objRDVM_21,objRDVDD_22,objRDDMP_23,objRDATMVPA_24,objRDVPKhH_25,objRDVPFBPYM_26,objRDVPVBF_27,objRDVPBKhA_28,objRDVBAA_29,objHBVAI_30,objEMHVBKD_31,objVTG_32,objEHVBKDF_33,objZEEVSBHG_34,objRTM_35,objTCMkD_36,objEAE_37,objEAEBK_38,objFDGASP_39,objFDGASPE_40,objVSHU_41,objMSchT_42,objpMRM_1_43,objpMRM_2_44]


                    return linksArray

            def arrayMsgFunc(self):
                    schVM_1 = "پاسخ مثبت درخواست های ویزای دانشجویی،‌دکترا، فرصت مطالعاتی و پژوهشی"
                    nV_2 = "نمونه وکالتنامه برای افراد پر سفر"
                    chLSCH_3 = "چک لیست روادید شنگن"
                    mSchDB_4 = "مدارک مورد نیاز ویزای شنگن(دیدار بستگان)"
                    mSchN_5 = "مدارک مورد نیاز ویزای شنگن (نمایشگاه)"
                    mSchT_6 = "مدارک مورد نیاز ویزای شنگن (تجاری)"
                    mSchMK_7 = "مدارک مورد نیاز ویزای شنگن (ماموریت کاری)"
                    mSchCS_8 = "مدارک مورد نیاز ویزای شنگن (کنگره و سمینار)"
                    mSchMV_9 = "مدارک مورد نیاز ویزای شنگن (مسابقه ورزشی)"
                    mSchT_10 = "مدارک مورد نیاز ویزای شنگن (ترانزیت)"
                    mSchD_11 = "مدارک مورد نیاز ویزای شنگن (درمان)"
                    mSchHB_12 = "مدارک مورد نیاز ویزای شنگن (به منظور همراهی بیمار در سفر)"
                    #shold change blank
                    pPS_13 = "عکس گذرنامه باید دارای چه شرایطی باشد، عکس های نمونه"

                    eRV_14 = "توضیحات در مورد برگه ابلاغیه رد درخواست روادید دریافتی"
                    fVN_15 = "فرم وکالتنامه جهت اعتراض"
                    fDV_16 = "فرم درخواست روادید(ویزا)"
                    rDVK_17 = "راهنمای درخواست روادید(ویزا) جهت اشتغال به کار"
                    rDVTSh_18 = "راهنمای درخواست روادید(ویزا) جهت تاسیس شرکت (کار آزاد)"
                    
                    rDVE_19 = "راهنمای درخواست روادید(ویزا) جهت ازدواج"
                    rDJK_20 = "راهنمای درخواست روادید(ویزا) جهت جستجوی کار"
                    rDVM_21 = "راهنمای درخواست روادید(ویزا) جهت ورود مجدد"
                    rDVDD_22 = "راهنمای درخواست روادید(ویزا) دانشجویی - دوره دکترا"
                    rDDMP_23 = "راهنمای درخواست روادید دانشجویی برای دانشمندان میهمان و پژوهشگران"
                    rDATMVPA_24 = "راهنمای درخواست روادید برای ارزشیابی و تایید مدارک آموزشی و پروانه اشتغال کسب شده در خارج از آلمان"
                    rDVPKhH_25 = "راهنمای درخواست روادید(ویزا) پیوست به خانواده به همسر ( و فرزندان همراه)"
                    rDVPFBPYM_26 = "راهنمای درخواست روادید(ویزا) پیوست فرزند به پدر یا مادر"
                    rDVPVBF_27 = "راهنمای درخواست روادید(ویزا) جهت پیوست والدین به فرزند"
                    rDVPBKhA_28 = "راهنمای درخواست روادید(ویزا) جهت پیوست به خانواده(افغانها)"
                    rDVBAA_29 = "برگه راهنما برای بررسی اسناد افغانی"
                    hBVAI_30 = "هزینه بررسی و رسیدگی رواید(ویزا) برای اتباع ایرانی"
                    eMHVBKD_31 = "اطلاعات مربوط به معافیت از هزینه ها و هزینه های روادید(ویزا) برای اتباع کشورهای دیگر"
                    vTG_32 = "وکالت نامه جهت تحویل گرفتن گذرنامه"
                    eHVBKDF_33 = "اطلاعات مربوط به معافیت از هزینه ها وهزینه های روادید برای اتباع کشورهای دیگر(فارسی)"
                    # zEEVSBHG_34 = "زمان های انتظار برای هر گروه جهت وقت سفارت"
                    rTM_35 = "برگه راهنما جهت تأیید مدارک"
                    tCMkD_36 = "تأیید و تصدیق کپی مدارک ایرانی، تذکر برای دانشجوها"
                    eAE_37 = "انصراف از ارث"
                    eAEBK_38 = "انصراف از ارث برای کودکان"
                    fDGASP_39 = "فرم درخواست صدور گواهی عدم سوءپیشینه(آلمانی)"
                    fDGASPE_40 = "فرم درخواست صدور گواهی عدم سوءپیشینه(انگلیسی)" 
                    vSHU_41 = "ورود و سفر عبوری با حیوانات خانگی در منطقه اتحادیه اروپا "
                    mSchT_42 = "مدارک مورد نیاز ویزای شنگن (توریست)"
                    
                    # pMRM_1_43 ="پاسخ مثپت روادیدهای ملی"
                    # pMRM_2_44 ="پاسخ مثپت روادیدهای ملی"

                    msgArray = [schVM_1,nV_2,chLSCH_3,mSchDB_4,mSchN_5,mSchT_6,mSchMK_7,mSchCS_8,mSchMV_9,mSchT_10,mSchD_11,mSchHB_12,pPS_13,eRV_14,fVN_15,fDV_16,rDVK_17,rDVTSh_18,rDVE_19,rDJK_20,rDVM_21,rDVDD_22,rDDMP_23,rDATMVPA_24,rDVPKhH_25,rDVPFBPYM_26,rDVPVBF_27,rDVPBKhA_28,rDVBAA_29,hBVAI_30,eMHVBKD_31,vTG_32,eHVBKDF_33,rTM_35,tCMkD_36,eAE_37,eAEBK_38,fDGASP_39,fDGASPE_40,vSHU_41,mSchT_42]
                    #zEEVSBHG_34
                    # msgArray = [schVM_1,nV_2,chLSCH_3,mSchDB_4,mSchN_5,mSchT_6,mSchMK_7,mSchCS_8,mSchMV_9,mSchT_10,mSchD_11,mSchHB_12,pPS_13,eRV_14,fVN_15,fDV_16,rDVK_17,rDVTSh_18,rDVE_19,rDJK_20,rDVM_21,rDVDD_22,rDDMP_23,rDATMVPA_24,rDVPKhH_25,rDVPFBPYM_26,rDVPVBF_27,rDVPBKhA_28,rDVBAA_29,hBVAI_30,eMHVBKD_31,vTG_32,eHVBKDF_33,zEEVSBHG_34,rTM_35,tCMkD_36,eAE_37,eAEBK_38,fDGASP_39,fDGASPE_40,vSHU_41,mSchT_42,pMRM_1_43,pMRM_2_44]

                    return msgArray
         
            def arrayAddMsgFunc(self):
                    addSchVM_1 = "سایت سفارت>>خدمات>>روادید و سفر >> روادید اقامت >> پاسخ مثبت درخواست های ویزای دانشجویی،‌دکترا، فرصت مطالعاتی و پژوهشی \n یا \n سایت سفارت>>خدمات >>روادیدوسفر>>روادید اقامت>>تحویل گرفتن روادید"
                    addNV_2 = "سایت سفارت>>خدمات >>روادیدوسفر>>روادید شنگن"
                    addChLSCH_3 = " سایت سفارت>>خدمات >>روادیدوسفر>>روادید شنگن>چک لیست های تنظیم مدارک(لینک موجود در متن صفحه)>>چه مدارکی باید ارایه کنم؟ (برگه های راهنما)"
                    addMSchDB_4 = " سایت سفارت>>خدمات >>روادیدوسفر>>روادید شنگن>چک لیست های تنظیم مدارک(لینک موجود در متن صفحه)>>چه مدارکی باید ارایه کنم؟ (برگه های راهنما)"
                    addMSchN_5 = " سایت سفارت>>خدمات >>روادیدوسفر>>روادید شنگن>چک لیست های تنظیم مدارک(لینک موجود در متن صفحه)>>چه مدارکی باید ارایه کنم؟ (برگه های راهنما)"
                    addMSchT_6 = " سایت سفارت>>خدمات >>روادیدوسفر>>روادید شنگن>چک لیست های تنظیم مدارک(لینک موجود در متن صفحه)>>چه مدارکی باید ارایه کنم؟ (برگه های راهنما)"
                    addMSchMK_7 = " سایت سفارت>>خدمات >>روادیدوسفر>>روادید شنگن>چک لیست های تنظیم مدارک(لینک موجود در متن صفحه)>>چه مدارکی باید ارایه کنم؟ (برگه های راهنما)"
                    addMSchCS_8 = " سایت سفارت>>خدمات >>روادیدوسفر>>روادید شنگن>چک لیست های تنظیم مدارک(لینک موجود در متن صفحه)>>چه مدارکی باید ارایه کنم؟ (برگه های راهنما)"
                    addMSchMV_9 = " سایت سفارت>>خدمات >>روادیدوسفر>>روادید شنگن>چک لیست های تنظیم مدارک(لینک موجود در متن صفحه)>>چه مدارکی باید ارایه کنم؟ (برگه های راهنما)"
                    addMSchT_10 = " سایت سفارت>>خدمات >>روادیدوسفر>>روادید شنگن>چک لیست های تنظیم مدارک(لینک موجود در متن صفحه)>>چه مدارکی باید ارایه کنم؟ (برگه های راهنما)"
                    addMSchD_11 = " سایت سفارت>>خدمات >>روادیدوسفر>>روادید شنگن>چک لیست های تنظیم مدارک(لینک موجود در متن صفحه)>>چه مدارکی باید ارایه کنم؟ (برگه های راهنما)"
                    addMSchHB_12 = " سایت سفارت>>خدمات >>روادیدوسفر>>روادید شنگن>چک لیست های تنظیم مدارک(لینک موجود در متن صفحه)>>چه مدارکی باید ارایه کنم؟ (برگه های راهنما)"
                    #shold change blank
                    addPPS_13 = "سایت سفارت>>خدمات >>روادیدوسفر>>روادید شنگن>چک لیست های تنظیم مدارک(لینک موجود در متن صفحه)>>چه مدارکی باید ارایه کنم؟ (برگه های راهنما)>>سؤالات متداول مربوط به مدارک/برگه های راهنما"

                    addERV_14 = "سایت سفارت>>خدمات >>روادیدوسفر>>روادید شنگن> عودت گذرنامه- ارائه اعتراض و شکایت حقوقی (لینک موجود در صفحه)>> ارايه اعتراض و شکایت حقوقی"
                    addFVN_15 = "سایت سفارت>>خدمات >>روادیدوسفر>>روادید شنگن> عودت گذرنامه- ارائه اعتراض و شکایت حقوقی (لینک موجود در صفحه)>> ارايه اعتراض و شکایت حقوقی"
                    addFDV_16 = "سایت سفارت>>خدمات >>روادیدوسفر>>روادید اقامت>>فرم درخواست"
                    addRDVK_17 = "سایت سفارت>>خدمات >>روادیدوسفر>>روادید اقامت>>چه مدارکی باید ارایه کنیم (برگه های راهنما)"
                    addRDVTSh_18 = "سایت سفارت>>خدمات >>روادیدوسفر>>روادید اقامت>>چه مدارکی باید ارایه کنیم (برگه های راهنما)"
                    addRDVE_19 = "سایت سفارت>>خدمات >>روادیدوسفر>>روادید اقامت>>چه مدارکی باید ارایه کنیم (برگه های راهنما)"
                    addRDJK_20 = "سایت سفارت>>خدمات >>روادیدوسفر>>روادید اقامت>>چه مدارکی باید ارایه کنیم (برگه های راهنما)"
                    addRDVM_21 = "سایت سفارت>>خدمات >>روادیدوسفر>>روادید اقامت>>چه مدارکی باید ارایه کنیم (برگه های راهنما)"
                    addRDVDD_22 = "سایت سفارت>>خدمات >>روادیدوسفر>>روادید اقامت>>چه مدارکی باید ارایه کنیم (برگه های راهنما) \n یا \n سایت سفارت>>خدمات >>روادیدوسفر>>روادید اقامت>>چه مدارکی باید ارایه کنیم (برگه های راهنما)>>پرسش های متداول پیرامون ویزای دانشجویی در اینجا"
                    addRDDMP_23 = "سایت سفارت>>خدمات >>روادیدوسفر>>روادید اقامت>>چه مدارکی باید ارایه کنیم (برگه های راهنما)"
                    addRDATMVPA_24 = "سایت سفارت>>خدمات >>روادیدوسفر>>روادید اقامت>>چه مدارکی باید ارایه کنیم (برگه های راهنما)"
                    addRDVPKhH_25 = "سایت سفارت>>خدمات >>روادیدوسفر>>روادید اقامت>>چه مدارکی باید ارایه کنیم (برگه های راهنما) \n یا \n سایت سفارت>>خدمات >>روادیدوسفر>>روادید اقامت>>چه مدارکی باید ارایه کنیم (برگه های راهنما)>>پرسش های متداول پیرامون ویزای دانشجویی در اینجا"
                    addRDVPFBPYM_26 = "سایت سفارت>>خدمات >>روادیدوسفر>>روادید اقامت>>چه مدارکی باید ارایه کنیم (برگه های راهنما)\n یا \n سایت سفارت>>خدمات >>روادیدوسفر>>روادید اقامت>>فرآیند روادید برای متقاضیان زیر ۱۸ سال"
                    addRDVPVBF_27 = "سایت سفارت>>خدمات >>روادیدوسفر>>روادید اقامت>>چه مدارکی باید ارایه کنیم (برگه های راهنما)"
                    addRDVPBKhA_28 = "سایت سفارت>>خدمات >>روادیدوسفر>>روادید اقامت>>چه مدارکی باید ارایه کنیم (برگه های راهنما)"
                    addRDVBAA_29 = "سایت سفارت>>خدمات >>روادیدوسفر>>روادید اقامت>>چه مدارکی باید ارایه کنیم (برگه های راهنما)"
                    addHBVAI_30 = "سایت سفارت>>خدمات >>روادیدوسفر>>روادید اقامت>>نحوه درخواست و بررسی درخواست روادید شما"
                    addEMHVBKD_31 = "سایت سفارت>>خدمات >>روادیدوسفر>>روادید اقامت>>نحوه درخواست و بررسی درخواست روادید شما"
                    addVTG_32 = " سایت سفارت>>خدمات >>روادیدوسفر>>روادید اقامت>>تحویل گرفتن روادید "
                    addEHVBKDF_33 = "سایت سفارت>>خدمات >>روادیدوسفر>>پرسش های مربوط به ویزا > هزینه بررسی و رسیدگی(موجود در متن صفحه در لیست کشویی)"
                    # addZEEVSBHG_34 = "سایت سفارت>>خدمات >>روادیدوسفر>>روادید اقامت"
                    addRTM_35 = "سایت سفارت>>خدمات >>تایید و تصدیق مدارک"
                    addTCMkD_36 = "سایت سفارت>>خدمات >>تایید و تصدیق مدارک "
                    addEAE_37 = "سایت سفارت>>خدمات >>تایید و تصدیق مدارک "
                    addEAEBK_38 = "سایت سفارت>>خدمات >>تایید و تصدیق مدارک "
                    addFDGASP_39 = "سایت سفارت>>خدمات >>گواهی عدم سوء پیشینه"
                    addFDGASPE_40 = "سایت سفارت>>خدمات >>گواهی عدم سوء پیشینه" 
                    addVSHU_41 = "سایت سفارت>>خدمات >>امور مربوط به گمرک"
                    addMSchT_42 = "سایت سفارت>>خدمات >>روادیدوسفر>>روادید شنگن>>چک لیست های تنظیم مدارک(لینک موجود در متن صفحه)>>چه مدارکی باید ارایه کنم؟ (برگه های راهنما)"
                    # addTest_43 = "تو سیستم localhost"
                    # addpPMRM_1_43 = "سایت سفارت>>خدمات >>روادیدوسفر>>روادید اقامت"
                    # addpPMRM_2_44 ="سایت سفارت>>خدمات >>روادیدوسفر>>روادید اقامت>>اقامت>>تحویل گرفتن روادید"

                    msgArray = [addSchVM_1,addNV_2,addChLSCH_3,addMSchDB_4,addMSchN_5,addMSchT_6,addMSchMK_7,addMSchCS_8,addMSchMV_9,addMSchT_10,addMSchD_11,addMSchHB_12,addPPS_13,addERV_14,addFVN_15,addFDV_16,addRDVK_17,addRDVTSh_18,addRDVE_19,addRDJK_20,addRDVM_21,addRDVDD_22,addRDDMP_23,addRDATMVPA_24,addRDVPKhH_25,addRDVPFBPYM_26,addRDVPVBF_27,addRDVPBKhA_28,addRDVBAA_29,addHBVAI_30,addEMHVBKD_31,addVTG_32,addEHVBKDF_33,addRTM_35,addTCMkD_36,addEAE_37,addEAEBK_38,addFDGASP_39,addFDGASPE_40,addVSHU_41,addMSchT_42]
                    #addZEEVSBHG_34,
                    # msgArray = [addSchVM_1,addNV_2,addChLSCH_3,addMSchDB_4,addMSchN_5,addMSchT_6,addMSchMK_7,addMSchCS_8,addMSchMV_9,addMSchT_10,addMSchD_11,addMSchHB_12,addPPS_13,addERV_14,addFVN_15,addFDV_16,addRDVK_17,addRDVTSh_18,addRDVE_19,addRDJK_20,addRDVM_21,addRDVDD_22,addRDDMP_23,addRDATMVPA_24,addRDVPKhH_25,addRDVPFBPYM_26,addRDVPVBF_27,addRDVPBKhA_28,addRDVBAA_29,addHBVAI_30,addEMHVBKD_31,addVTG_32,addEHVBKDF_33,addZEEVSBHG_34,addRTM_35,addTCMkD_36,addEAE_37,addEAEBK_38,addFDGASP_39,addFDGASPE_40,addVSHU_41,addMSchT_42,addpPMRM_1_43,addpPMRM_2_44]


                    return msgArray

class CurrentContainerClass:
    
            def scrap(self,url):
                    uClient = uReq(url)
                    spage_html = uClient.read()
                    uClient.close()

                    #html parser
                    page_soup = soup(spage_html,"html.parser")
                    return page_soup
            

            # @classmethod
            def schulerVisum(self):
                #1  
                #  پاسخ مثبت درخواست های ویزای دانشجویی،‌دکترا، فرصت مطالعاتی و پژوهشی
                # checked Address tree and title and address tree link ok!
                # وب سایت سفارت آلمان>>خدمات>>روادید و سفر >> روادید اقامت >> پاسخ مثبت درخواست های ویزای دانشجویی،‌دکترا، فرصت مطالعاتی و پژوهشی
                    # my_url = "https://teheran.diplo.de/ir-fa/service/visa-einreise/-/2077426"
                    my_url = "https://teheran.diplo.de/ir-fa/service/visa-einreise/-/1906462"
                    #opening up connection and grabing the page
                    myPageSoup = self.scrap(my_url)
                    #grabs each 
                    container= myPageSoup.findAll("a",{"class":"rte__anchor i-pdf"})[0]["href"]
                    print("1 schulerVisum() has scraped ")
                    return container
            # other address to take the file پاسخ مثبت درخواست های ویزای دانشجویی،‌دکترا، فرصت مطالعاتی و پژوهشی is
            #سایت سفارت>>خدمات >>روادیدوسفر>>روادید اقامت>>اقامت>>تحویل گرفتن روادید
            # https://teheran.diplo.de/ir-fa/service/visa-einreise/-/2074660

            # my_url = "https://teheran.diplo.de/ir-fa/service/visa-einreise/-/1906462"
            #     #opening up connection and grabing the page
            #     myPageSoup = self.scrap(my_url)
            #     #grabs each 
            #     container = myPageSoup.findAll("a",{"class":"rte__anchor i-pdf"})[0]["href"]


            def nemuneVekalat(self):
                #2
                #نکاتی برای "افراد پرسفر")(نمونه چنین وکالتنامه ای
                # checked Address tree and title and address tree link ok!
                # سایت سفارت>>خدمات >>روادیدوسفر>>روادید شنگن
                    my_url = "https://teheran.diplo.de/ir-fa/service/visa-einreise/-/1906470"
                    #opening up connection and grabing the page
                    myPageSoup = self.scrap(my_url)
                    #grabs each 
                    container= myPageSoup.findAll("a",{"class":"rte__anchor i-pdf"})[0]["href"]
                    print("2 nemuneVekalat() has scraped ")
                    return "https://teheran.diplo.de"+container

            def checkListSchengen(self):
                #3
                #چک لیست روادید شنگن 
                # checked Address tree and title and address tree link ok!
                # سایت سفارت>>خدمات >>روادیدوسفر>>روادید شنگن>چک لیست های تنظیم مدارک(لینک موجود در متن صفحه)>>چه مدارکی باید ارایه کنم؟ (برگه های راهنما)
                    my_url = "https://teheran.diplo.de/ir-fa/service/visa-einreise/-/2074662"
                    #opening up connection and grabing the page
                    myPageSoup = self.scrap(my_url)
                    #grabs each 
                    container= myPageSoup.findAll("a",{"class":"rte__anchor i-pdf"})[0]["href"]
                    print("3 checkListSchengen() has scraped ")
                    return "https://teheran.diplo.de"+container

            def madarekSchengenDidarBastegan(self):
                #4
                #مدارک مورد نیاز ویزای شنگن (دیدار بستگان)
                # checked Address tree and title and address tree link ok!
                # سایت سفارت>>خدمات >>روادیدوسفر>>روادید شنگن>چک لیست های تنظیم مدارک(لینک موجود در متن صفحه)>>چه مدارکی باید ارایه کنم؟ (برگه های راهنما)
                    my_url = "https://teheran.diplo.de/ir-fa/service/visa-einreise/-/2074662"
                    #opening up connection and grabing the page
                    myPageSoup = self.scrap(my_url)
                    #grabs each 
                    container= myPageSoup.findAll("a",{"class":"rte__anchor i-pdf"})[1]["href"]
                    print("4 madarekSchengenDidarBastegan() has scraped ")
                    return "https://teheran.diplo.de"+container

            def madarekSchengenNamaeshgah(self):
                #5
                # مدارک مورد نیاز ویزای شنگن (نمایشگاه)
                # checked Address tree and title and address tree link ok!
                # سایت سفارت>>خدمات >>روادیدوسفر>>روادید شنگن>چک لیست های تنظیم مدارک(لینک موجود در متن صفحه)>>چه مدارکی باید ارایه کنم؟ (برگه های راهنما)
                    my_url = "https://teheran.diplo.de/ir-fa/service/visa-einreise/-/2074662"
                    #opening up connection and grabing the page
                    myPageSoup = self.scrap(my_url)
                    #grabs each 
                    container= myPageSoup.findAll("a",{"class":"rte__anchor i-pdf"})[2]["href"]
                    print("5 madarekSchengenNamaeshgah() has scraped")
                    return "https://teheran.diplo.de"+container

            
            
            def madarekSchengenTejari(self):
                #6
                # مدارک مورد نیاز ویزای شنگن (تجاری)
                # checked Address tree and title and address tree link ok!
                # سایت سفارت>>خدمات >>روادیدوسفر>>روادید شنگن>چک لیست های تنظیم مدارک(لینک موجود در متن صفحه)>>چه مدارکی باید ارایه کنم؟ (برگه های راهنما)
                    my_url = "https://teheran.diplo.de/ir-fa/service/visa-einreise/-/2074662"
                    #opening up connection and grabing the page
                    myPageSoup = self.scrap(my_url)
                    #grabs each 
                    container= myPageSoup.findAll("a",{"class":"rte__anchor i-pdf"})[4]["href"]
                    print("6 madarekSchengenTejari() has scraped")
                    return "https://teheran.diplo.de"+container            

            def madarekSchengenMamurKari(self):
                #7
                # مدارک مورد نیاز ویزای شنگن (ماموریت کاری)
                # checked Address tree and title and address tree link ok!
                # سایت سفارت>>خدمات >>روادیدوسفر>>روادید شنگن>چک لیست های تنظیم مدارک(لینک موجود در متن صفحه)>>چه مدارکی باید ارایه کنم؟ (برگه های راهنما)
                    my_url = "https://teheran.diplo.de/ir-fa/service/visa-einreise/-/2074662"
                    #opening up connection and grabing the page
                    myPageSoup = self.scrap(my_url)
                    #grabs each 
                    container= myPageSoup.findAll("a",{"class":"rte__anchor i-pdf"})[5]["href"]
                    print("7 madarekSchengenMamurKari() has scraped")
                    return "https://teheran.diplo.de"+container      

            def madarekSchengenCongressSeminar(self):
                #8
                # مدارک مورد نیاز ویزای شنگن (کنگره و سمینار)
                # checked Address tree and title and address tree link ok!
                # سایت سفارت>>خدمات >>روادیدوسفر>>روادید شنگن>چک لیست های تنظیم مدارک(لینک موجود در متن صفحه)>>چه مدارکی باید ارایه کنم؟ (برگه های راهنما)
                    my_url = "https://teheran.diplo.de/ir-fa/service/visa-einreise/-/2074662"
                    #opening up connection and grabing the page
                    myPageSoup = self.scrap(my_url)
                    #grabs each 
                    container= myPageSoup.findAll("a",{"class":"rte__anchor i-pdf"})[6]["href"]
                    print("8 madarekSchengenCongressSeminar() has scraped")
                    return "https://teheran.diplo.de"+container  

            def madarekSchengenMosabeghVarzeshi(self):
                #9
                # مدارک مورد نیاز ویزای شنگن (مسابقه ورزشی)
                # checked Address tree and title and address tree link ok!
                # سایت سفارت>>خدمات >>روادیدوسفر>>روادید شنگن>چک لیست های تنظیم مدارک(لینک موجود در متن صفحه)>>چه مدارکی باید ارایه کنم؟ (برگه های راهنما)
                    my_url = "https://teheran.diplo.de/ir-fa/service/visa-einreise/-/2074662"
                    #opening up connection and grabing the page
                    myPageSoup = self.scrap(my_url)
                    #grabs each 
                    container= myPageSoup.findAll("a",{"class":"rte__anchor i-pdf"})[7]["href"]
                    print("9 madarekSchengenMosabeghVarzeshi() has scraped")
                    return "https://teheran.diplo.de"+container 

            def madarekSchengenTransit(self):
                #10
                # مدارک مورد نیاز ویزای شنگن (ترانزیت)
                # checked Address tree and title and address tree link ok!
                # سایت سفارت>>خدمات >>روادیدوسفر>>روادید شنگن>چک لیست های تنظیم مدارک(لینک موجود در متن صفحه)>>چه مدارکی باید ارایه کنم؟ (برگه های راهنما)
                    my_url = "https://teheran.diplo.de/ir-fa/service/visa-einreise/-/2074662"
                    #opening up connection and grabing the page
                    myPageSoup = self.scrap(my_url)
                    #grabs each 
                    container= myPageSoup.findAll("a",{"class":"rte__anchor i-pdf"})[8]["href"]
                    print("10 madarekSchengenTransit() has scraped")
                    return "https://teheran.diplo.de"+container 

            def madarekSchengenDarman(self):
                #11
                # مدارک مورد نیاز ویزای شنگن (درمان)
                #  checked Address tree and title and address tree link ok!
                # سایت سفارت>>خدمات >>روادیدوسفر>>روادید شنگن>چک لیست های تنظیم مدارک(لینک موجود در متن صفحه)>>چه مدارکی باید ارایه کنم؟ (برگه های راهنما)
                    my_url = "https://teheran.diplo.de/ir-fa/service/visa-einreise/-/2074662"
                    #opening up connection and grabing the page
                    myPageSoup = self.scrap(my_url)
                    #grabs each 
                    container= myPageSoup.findAll("a",{"class":"rte__anchor i-pdf"})[9]["href"]
                    print("11 madarekSchengenDarman() has scraped")
                    return "https://teheran.diplo.de"+container 

            def madarekSchengenHamrahiBimar(self):
                #12
                # مدارک مورد نیاز ویزای شنگن (به منظور همراهی بیمار در سفر)
                #  checked Address tree and title and address tree link ok!
                # سایت سفارت>>خدمات >>روادیدوسفر>>روادید شنگن>چک لیست های تنظیم مدارک(لینک موجود در متن صفحه)>>چه مدارکی باید ارایه کنم؟ (برگه های راهنما)
                    my_url = "https://teheran.diplo.de/ir-fa/service/visa-einreise/-/2074662"
                    #opening up connection and grabing the page
                    myPageSoup = self.scrap(my_url)
                    #grabs each 
                    container= myPageSoup.findAll("a",{"class":"rte__anchor i-pdf"})[10]["href"]
                    print("12 madarekSchengenHamrahiBimar() has scraped")
                    return "https://teheran.diplo.de"+container 

            def photoPassSample(self):
                #13
                # عکس گذرنامه باید دارای چه شرایطی باشد، عکس های نمونه
                #  checked Address tree and title and address tree link ok!
                # سایت سفارت>>خدمات >>روادیدوسفر>>روادید شنگن>چک لیست های تنظیم مدارک(لینک موجود در متن صفحه)>>چه مدارکی باید ارایه کنم؟ (برگه های راهنما)>>سؤالات متداول مربوط به مدارک/برگه های راهنما
                    my_url = "https://teheran.diplo.de/ir-fa/service/visa-einreise/-/1906472"
                    #opening up connection and grabing the page
                    myPageSoup = self.scrap(my_url)
                    #grabs each 
                    container= myPageSoup.findAll("a",{"class":"rte__anchor i-pdf"})[0]["href"]
                    print("13 photoPassSample() has scraped")
                    return container 

            def explanationRejectVisa(self):
                #14
                # توضیحات در مورد برگه ابلاغیه رد درخواست روادید دریافتی
                #  checked Address tree and title and address tree link ok!
                #  سایت سفارت>>خدمات >>روادیدوسفر>>روادید شنگن> عودت گذرنامه- ارائه اعتراض و شکایت حقوقی (لینک موجود در صفحه)>> ارايه اعتراض و شکایت حقوقی
                    my_url = "https://teheran.diplo.de/ir-fa/service/visa-einreise/-/2074666"
                    #opening up connection and grabing the page
                    myPageSoup = self.scrap(my_url)
                    #grabs each 
                    container= myPageSoup.findAll("a",{"class":"rte__anchor i-pdf"})[0]["href"]
                    print("14 explanationRejectVisa() has scraped")
                    return "https://teheran.diplo.de"+container 
            
            def formVekalatNameh(self):
                #15
                # فرم وکالتنامه جهت اعتراض
                #  checked Address tree and title and address tree link ok!
                #  سایت سفارت>>خدمات >>روادیدوسفر>>روادید شنگن> عودت گذرنامه- ارائه اعتراض و شکایت حقوقی (لینک موجود در صفحه)>> ارايه اعتراض و شکایت حقوقی
                    my_url = "https://teheran.diplo.de/ir-fa/service/visa-einreise/-/2074666"
                    #opening up connection and grabing the page
                    myPageSoup = self.scrap(my_url)
                    #grabs each 
                    container= myPageSoup.findAll("a",{"class":"rte__anchor i-pdf"})[1]["href"]
                    print("15 formVekalatNameh() has scraped")
                    return container 

            def formDarkhastVisa(self):
                #16
                # فرم درخواست روادید(ویزا)
                #  checked Address tree and title and address tree link ok!
                #  سایت سفارت>>خدمات >>روادیدوسفر>>روادید اقامت>>فرم درخواست
                    my_url = "https://teheran.diplo.de/ir-fa/service/visa-einreise/-/2073844"
                    #opening up connection and grabing the page
                    myPageSoup = self.scrap(my_url)
                    #grabs each 
                    container= myPageSoup.findAll("a",{"class":"rte__anchor i-pdf"})[0]["href"]
                    print("16 formDarkhastVisa() has scraped")
                    return "https://teheran.diplo.de" + container 


            def rahnamaDarkhastVisaKar(self):
                #17
                # راهنمای درخواست روادید(ویزا) جهت اشتغال به کار
                #  checked Address tree and title and address tree link ok!
                #  سایت سفارت>>خدمات >>روادیدوسفر>>روادید اقامت>>چه مدارکی باید ارایه کنیم (برگه های راهنما(
                    my_url = "https://teheran.diplo.de/ir-fa/service/visa-einreise/-/2073766"
                    #opening up connection and grabing the page
                    myPageSoup = self.scrap(my_url)
                    #grabs each 
                    container= myPageSoup.findAll("a",{"class":"rte__anchor i-pdf"})[0]["href"]
                    print("17 rahnamaDarkhastVisaKar() has scraped")
                    return "https://teheran.diplo.de" + container 

            def rahnamaDarkhastVisaTasisSherkat(self):
                #18
                # راهنمای درخواست روادید جهت تاسیس شرکت (کار آزاد)
                #  checked Address tree and title and address tree link ok!
                #  سایت سفارت>>خدمات >>روادیدوسفر>>روادید اقامت>>چه مدارکی باید ارایه کنیم (برگه های راهنما(
                    my_url = "https://teheran.diplo.de/ir-fa/service/visa-einreise/-/2073766"
                    #opening up connection and grabing the page
                    myPageSoup = self.scrap(my_url)
                    #grabs each 
                    container= myPageSoup.findAll("a",{"class":"rte__anchor i-pdf"})[1]["href"]
                    print("18 rahnamaDarkhastVisaTasisSherkat() has scraped")
                    return "https://teheran.diplo.de" + container

            def rahnamaDarkhastVisaEzdevaj(self):
                #19
                # راهنمای درخواست روادید(ویزا) جهت ازدواج
                #  checked Address tree and title and address tree link ok!
                #  سایت سفارت>>خدمات >>روادیدوسفر>>روادید اقامت>>چه مدارکی باید ارایه کنیم (برگه های راهنما(
                    my_url = "https://teheran.diplo.de/ir-fa/service/visa-einreise/-/2073766"
                    #opening up connection and grabing the page
                    myPageSoup = self.scrap(my_url)
                    #grabs each 
                    container= myPageSoup.findAll("a",{"class":"rte__anchor i-pdf"})[2]["href"]
                    print("19 rahnamaDarkhastVisaEzdevaj() has scraped")
                    return "https://teheran.diplo.de" + container

            def rahnamaDarkhastJostejuyeKar(self):
                #20
                # راهنمای درخواست روادید(ویزا) جهت جستجوی کار
                #  checked Address tree and title and address tree link ok!
                #  سایت سفارت>>خدمات >>روادیدوسفر>>روادید اقامت>>چه مدارکی باید ارایه کنیم (برگه های راهنما(
                    my_url = "https://teheran.diplo.de/ir-fa/service/visa-einreise/-/2073766"
                    #opening up connection and grabing the page
                    myPageSoup = self.scrap(my_url)
                    #grabs each 
                    container= myPageSoup.findAll("a",{"class":"rte__anchor i-pdf"})[3]["href"]
                    print("20 rahnamaDarkhastJostejuyeKar() has scraped")
                    return "https://teheran.diplo.de" + container

            def rahnamaDarkhastVorudMojadad(self):
                #21
                # راهنمای درخواست روادید(ویزا) جهت ورود مجدد
                #  checked Address tree and title and address tree link ok!
                #  سایت سفارت>>خدمات >>روادیدوسفر>>روادید اقامت>>چه مدارکی باید ارایه کنیم (برگه های راهنما(
                    my_url = "https://teheran.diplo.de/ir-fa/service/visa-einreise/-/2073766"
                    #opening up connection and grabing the page
                    myPageSoup = self.scrap(my_url)
                    #grabs each 
                    container= myPageSoup.findAll("a",{"class":"rte__anchor i-pdf"})[4]["href"]
                    print("21 rahnamaDarkhastVorudMojadad() has scraped")
                    return "https://teheran.diplo.de" + container

            def rahnamaDarkhastVisaDaneshjooDoctora(self):
                #22
                # راهنمای درخواست روادید(ویزا) دانشجویی - دوره دکترا
                #  checked Address tree and title and address tree link ok!
                #  سایت سفارت>>خدمات >>روادیدوسفر>>روادید اقامت>>چه مدارکی باید ارایه کنیم (برگه های راهنما(
                    my_url = "https://teheran.diplo.de/ir-fa/service/visa-einreise/-/2073766"
                    #opening up connection and grabing the page
                    myPageSoup = self.scrap(my_url)
                    #grabs each 
                    container= myPageSoup.findAll("a",{"class":"rte__anchor i-pdf"})[5]["href"]
                    print("22 rahnamaDarkhastVisaDaneshjooDoctora() has scraped")
                    return "https://teheran.diplo.de" + container
            # other address to take the file راهنمای درخواست روادید(ویزا) پیوست به خانواده به همسر ( و فرزندان همراه) is
            # سایت سفارت>>خدمات >>روادیدوسفر>>روادید اقامت>>چه مدارکی باید ارایه کنیم (برگه های راهنما)>>پرسش های متداول پیرامون ویزای دانشجویی در اینجا
            # https://teheran.diplo.de/ir-fa/service/visa-einreise/-/1906464
        

            def rahnamaDarkhastDaneshmandanMihmanPajooheshgaran(self):
                #23
                # راهنمای درخواست روادید دانشجویی برای دانشمندان میهمان و پژوهشگران
                #  checked Address tree and title and address tree link ok!
                #  سایت سفارت>>خدمات >>روادیدوسفر>>روادید اقامت>>چه مدارکی باید ارایه کنیم (برگه های راهنما(
                    my_url = "https://teheran.diplo.de/ir-fa/service/visa-einreise/-/2073766"
                    #opening up connection and grabing the page
                    myPageSoup = self.scrap(my_url)
                    #grabs each 
                    container= myPageSoup.findAll("a",{"class":"rte__anchor i-pdf"})[6]["href"]
                    print("23 rahnamaDarkhastDaneshmandanMihmanPajooheshgaran() has scraped")
                    return "https://teheran.diplo.de" + container

            def rahnamaDarkhastArzeshyabiTaidMadarekVaParvanehKharejAlman(self):
                #24
                # راهنمای درخواست روادید برای ارزشیابی و تایید مدارک آموزشی و پروانه اشتغال کسب شده در خارج از آلمان
                #  checked Address tree and title and address tree link ok!
                #  سایت سفارت>>خدمات >>روادیدوسفر>>روادید اقامت>>چه مدارکی باید ارایه کنیم (برگه های راهنما(
                    my_url = "https://teheran.diplo.de/ir-fa/service/visa-einreise/-/2073766"
                    #opening up connection and grabing the page
                    myPageSoup = self.scrap(my_url)
                    #grabs each
                    container = myPageSoup.findAll("a",{"class":"rte__anchor i-pdf"})[7]["href"]
                    print("24 rahnamaDarkhastArzeshyabiTaidMadarekVaParvanehKharejAlman() has scraped")
                    return "https://teheran.diplo.de" + container

            def rahnamaDarkhastVisaPeywastKhanevadehHamsar(self):
                #25
                # راهنمای درخواست روادید(ویزا) پیوست به خانواده به همسر ( و فرزندان همراه)
                #  checked Address tree and title and address tree link ok!
                #  سایت سفارت>>خدمات >>روادیدوسفر>>روادید اقامت>>چه مدارکی باید ارایه کنیم (برگه های راهنما(
                    my_url = "https://teheran.diplo.de/ir-fa/service/visa-einreise/-/2073766"
                    #opening up connection and grabing the page
                    myPageSoup = self.scrap(my_url)
                    #grabs each
                    container = myPageSoup.findAll("a",{"class":"rte__anchor i-pdf"})[8]["href"]
                    print("25 rahnamaDarkhastVisaPeywastKhanevadehHamsar() has scraped")
                    return "https://teheran.diplo.de" + container
            # other address to take the file راهنمای درخواست روادید(ویزا) پیوست به خانواده به همسر ( و فرزندان همراه) is
            # سایت سفارت>>خدمات >>روادیدوسفر>>روادید اقامت>>چه مدارکی باید ارایه کنیم (برگه های راهنما)>>پرسش های متداول پیرامون ویزای دانشجویی در اینجا"
            # https://teheran.diplo.de/ir-fa/service/visa-einreise/-/1906464


            def rahnamaDarkhastVisaPeywastFarzandBePedarYaMadar(self):
                #26
                # راهنمای درخواست روادید(ویزا) پیوست فرزند به پدر یا مادر
                #  checked Address tree and title and address tree link ok!
                #  سایت سفارت>>خدمات >>روادیدوسفر>>روادید اقامت>>چه مدارکی باید ارایه کنیم (برگه های راهنما(
                    my_url = "https://teheran.diplo.de/ir-fa/service/visa-einreise/-/2073766"
                    #opening up connection and grabing the page
                    myPageSoup = self.scrap(my_url)
                    #grabs each
                    container = myPageSoup.findAll("a",{"class":"rte__anchor i-pdf"})[9]["href"]
                    print("26 rahnamaDarkhastVisaPeywastFarzandBePedarYaMadar() has scraped")
                    return "https://teheran.diplo.de" + container
            # other address to take the file راهنمای درخواست روادید(ویزا) پیوست فرزند به پدر یا مادر is
            # سایت سفارت>>خدمات >>روادیدوسفر>>روادید اقامت>>فرآیند روادید برای متقاضیان زیر 18 سال 
            # https://teheran.diplo.de/ir-fa/service/visa-einreise/-/2074650



            def rahnamaDarkhastVisaPeywastValedeinBeFarzand(self):
                #27
                # راهنمای درخواست روادید(ویزا) جهت پیوست والدین به فرزند
                #  checked Address tree and title and address tree link ok!
                #  سایت سفارت>>خدمات >>روادیدوسفر>>روادید اقامت>>چه مدارکی باید ارایه کنیم (برگه های راهنما(
                    my_url = "https://teheran.diplo.de/ir-fa/service/visa-einreise/-/2073766"
                    #opening up connection and grabing the page
                    myPageSoup = self.scrap(my_url)
                    #grabs each 
                    container = myPageSoup.findAll("a",{"class":"rte__anchor i-pdf"})[10]["href"]
                    print("27 rahnamaDarkhastVisaPeywastValedeinBeFarzand() has scraped")
                    return "https://teheran.diplo.de" + container

            def rahnamaDarkhastVisaPeywastBeKhanevadehAfghanha(self):
                #28
                # راهنمای درخواست روادید(ویزا) جهت پیوست به خانواده(افغانها)
                #  checked Address tree and title and address tree link ok!
                #  سایت سفارت>>خدمات >>روادیدوسفر>>روادید اقامت>>چه مدارکی باید ارایه کنیم (برگه های راهنما(
                    my_url = "https://teheran.diplo.de/ir-fa/service/visa-einreise/-/2073766"
                    #opening up connection and grabing the page
                    myPageSoup = self.scrap(my_url)
                    #grabs each
                    container = myPageSoup.findAll("a",{"class":"rte__anchor i-pdf"})[11]["href"]
                    print("28 rahnamaDarkhastVisaPeywastBeKhanevadehAfghanha() has scraped")
                    return "https://teheran.diplo.de" + container

            def rahnamaDarkhastVisaBaresiAsnadAfghani(self):
                #29
                #  برگه راهنما برای بررسی اسناد افغانی
                #  checked Address tree and title and address tree link ok!
                #  سایت سفارت>>خدمات >>روادیدوسفر>>روادید اقامت>>چه مدارکی باید ارایه کنیم (برگه های راهنما(
                    my_url = "https://teheran.diplo.de/ir-fa/service/visa-einreise/-/2073766"
                    #opening up connection and grabing the page
                    myPageSoup = self.scrap(my_url)
                    #grabs each
                    container = myPageSoup.findAll("a",{"class":"rte__anchor i-pdf"})[12]["href"]
                    print("29 rahnamaDarkhastVisaBaresiAsnadAfghani() has scraped")
                    return "https://teheran.diplo.de" + container



            def hazinehBarresiVisaAtbaIrani(self):
                #30
                # هزینه بررسی و رسیدگی رواید(ویزا) برای اتباع ایرانی
                # checked Address tree and title and address tree link ok!
                #  سایت سفارت>>خدمات >>روادیدوسفر>>روادید اقامت>>نحوه درخواست و بررسی درخواست روادید شما
                    my_url = "https://teheran.diplo.de/ir-fa/service/visa-einreise/-/2074628"
                    #opening up connection and grabing the page
                    myPageSoup = self.scrap(my_url)
                    #grabs each
                    container = myPageSoup.findAll("a",{"class":"rte__anchor i-pdf"})[0]["href"]
                    print("30 hazinehBarresiVisaAtbaIrani() has scraped")
                    return container


            def etelatMafiatHazinehayeVisaBarayeKeshvarhayeDigar(self):
                #31
                # اطلاعات مربوط به معافیت از هزینه ها و هزینه های روادید برای اتباع کشورهای دیگر
                # checked Address tree and title and address tree link ok!
                #  سایت سفارت>>خدمات >>روادیدوسفر>>روادید اقامت>>نحوه درخواست و بررسی درخواست روادید شما
                    my_url = "https://teheran.diplo.de/ir-fa/service/visa-einreise/-/2074628"
                    #opening up connection and grabing the page
                    myPageSoup = self.scrap(my_url)
                    #grabs each
                    container = myPageSoup.findAll("a",{"class":"rte__anchor i-pdf"})[1]["href"]
                    print("31 etelatMafiatHazinehayeVisaBarayeKeshvarhayeDigar() has scraped")
                    return container

            def vekalatnameTahvilGozarnameh(self):
                #32
                # وکالت نامه جهت تحویل گرفتن گذرنامه
                # checked Address tree and title and address tree link ok!
                #  سایت سفارت>>خدمات >>روادیدوسفر>>روادید اقامت>>اقامت>>تحویل گرفتن روادید
                    my_url = "https://teheran.diplo.de/ir-fa/service/visa-einreise/-/2074660"
                    #opening up connection and grabing the page
                    myPageSoup = self.scrap(my_url)
                    #grabs each 
                    container = myPageSoup.findAll("a",{"class":"rte__anchor i-pdf"})[1]["href"]
                    print("32 vekalatnameTahvilGozarnameh() has scraped")
                    return container

            def etelatMafiatHazinehayeVisaBarayeKeshvarhayeDigarFarsi(self):
                #33
                # اطلاعات مربوط به معافیت از هزینه ها وهزینه های روادید برای اتباع کشورهای دیگر(فارسی)
                # checked Address tree and title and address tree link ok!
                #  سایت سفارت>>خدمات >>روادیدوسفر>>پرسش های مربوط به ویزا > هزینه بررسی و رسیدگی(موجود در متن صفحه در لیست کشویی)
                    my_url = "https://teheran.diplo.de/ir-fa/service/visa-einreise/-/1906474?openAccordionId=item-2080734-3-panel"
                    #opening up connection and grabing the page
                    myPageSoup = self.scrap(my_url)
                    #grabs each 
                    container = myPageSoup.findAll("a",{"class":"rte__anchor i-pdf"})[1]["href"]
                    print("33 etelatMafiatHazinehayeVisaBarayeKeshvarhayeDigarFarsi() has scraped")
                    return "https://teheran.diplo.de" + container

            def zamanEhtemaliEntezarVaghtSefaratBarayeHarGrouh(self):
                #34
                # زمان های انتظار برای هر گروه جهت وقت سفارت
                # زمان احتمالی وقت سفارت برای ارائه درخواست روادید ملی بعد از ثبت نام در لیست انتظار
                # checked Address tree and title and address tree link ok!
                #  سایت سفارت>>خدمات >>روادیدوسفر>>روادید اقامت
                    my_url = "https://teheran.diplo.de/ir-fa/service/visa-einreise/-/1906462"
                    
                    #opening up connection and grabing the page
                    myPageSoup = self.scrap(my_url)
                    #grabs each 
                    container = myPageSoup.findAll("a",{"class":"rte__anchor i-pdf"})[0]["href"]
                    print("34 zamanEhtemaliEntezarVaghtSefaratBarayeHarGrouh() has scraped")
                    return container

            def rahnameTaidMadarek(self):
                #35
                # برگه راهنما جهت تأیید مدارک
                # checked Address tree and title and address tree link ok!
                #  سایت سفارت>>خدمات >>تأیید و تصدیق مدارک
                    my_url = "https://teheran.diplo.de/ir-fa/service/-/1906482"
                    #opening up connection and grabing the page
                    myPageSoup = self.scrap(my_url)
                    #grabs each 
                    container = myPageSoup.findAll("a",{"class":"rte__anchor i-pdf"})[0]["href"]
                    print("35 rahnameTaidMadarek() has scraped")
                    return "https://teheran.diplo.de" + container

            def taidCopyMadrakDaneshjoo(self):
                #36
                # تأیید و تصدیق کپی مدارک ایرانی، تذکر برای دانشجوها
                # checked Address tree and title and address tree link ok!
                #  سایت سفارت>>خدمات >>تأیید و تصدیق مدارک
                    my_url = "https://teheran.diplo.de/ir-fa/service/-/1906482"
                    #opening up connection and grabing the page
                    myPageSoup = self.scrap(my_url)
                    #grabs each 
                    container = myPageSoup.findAll("a",{"class":"rte__anchor i-pdf"})[1]["href"]
                    print("36 taidCopyMadrakDaneshjoo() has scraped")
                    return "https://teheran.diplo.de" + container

            def enserafAzErs(self):
                #37
                # انصراف از ارث
                # checked Address tree and title and address tree link ok!
                #  سایت سفارت>>خدمات >>تأیید و تصدیق مدارک
                    my_url = "https://teheran.diplo.de/ir-fa/service/-/1906482"
                    #opening up connection and grabing the page
                    myPageSoup = self.scrap(my_url)
                    #grabs each 
                    container = myPageSoup.findAll("a",{"class":"rte__anchor i-pdf"})[3]["href"]
                    print("37 enserafAzErs() has scraped")
                    return "https://teheran.diplo.de" + container

            def enserafAzErsBarayeKoodakan(self):
                #38
                #  انصراف از ارث برای کودکان
                # checked Address tree and title and address tree link ok!
                #  سایت سفارت>>خدمات >>تأیید و تصدیق مدارک
                    my_url = "https://teheran.diplo.de/ir-fa/service/-/1906482"
                    #opening up connection and grabing the page
                    myPageSoup = self.scrap(my_url)
                    #grabs each 
                    container = myPageSoup.findAll("a",{"class":"rte__anchor i-pdf"})[4]["href"]
                    print("38 enserafAzErsBarayeKoodakan() has scraped")
                    return "https://teheran.diplo.de" + container

            def formDarkhastGovahiAdamSuePishineh(self):
                #39
                #  فرم درخواست صدور گواهی عدم سوءپیشینه(آلمانی)
                # checked Address tree and title and address tree link ok!
                #  سایت سفارت>>خدمات >>گواهی عدم سوء پیشینه
                    my_url = "https://teheran.diplo.de/ir-fa/service/-/1906488"
                    #opening up connection and grabing the page
                    myPageSoup = self.scrap(my_url)
                    #grabs each 
                    container = myPageSoup.findAll("a",{"class":"rte__anchor i-pdf"})[0]["href"]
                    print("39 formDarkhastGovahiAdamSuePishineh() has scraped")
                    return "https://teheran.diplo.de" + container

            def formDarkhastGovahiAdamSuePishinehEnglish(self):
                #40
                #  فرم درخواست صدور گواهی عدم سوءپیشینه(انگلیسی)
                # checked Address tree and title and address tree link ok!
                #  سایت سفارت>>خدمات >>گواهی عدم سوء پیشینه
                    my_url = "https://teheran.diplo.de/ir-fa/service/-/1906488"
                    #opening up connection and grabing the page
                    myPageSoup = self.scrap(my_url)
                    #grabs each 
                    container = myPageSoup.findAll("a",{"class":"rte__anchor i-pdf"})[1]["href"]
                    print("40 formDarkhastGovahiAdamSuePishinehEnglish() has scraped")
                    return "https://teheran.diplo.de" + container

            def vorudSafarHeywanatUropa(self):
                #41
                #  ورود و سفر عبوری با حیوانات خانگی در منطقه اتحادیه اروپا اطلاعات بیشتر
                # checked Address tree and title and address tree link ok!
                #  سایت سفارت>>خدمات >>امور مربوط به گمرک
                    my_url = "https://teheran.diplo.de/ir-fa/service/-/1906496"
                    #opening up connection and grabing the page
                    myPageSoup = self.scrap(my_url)
                    #grabs each 
                    container = myPageSoup.findAll("a",{"class":"rte__anchor i-pdf"})[0]["href"]
                    print("41 vorudSafarHeywanatUropa() has scraped")
                    return "https://teheran.diplo.de" + container

            def madarekSchengenTursist(self):
                #42
                # مدارک مورد نیاز ویزای شنگن (توریست)
                # checked Address tree and title and address tree link ok!
                # سایت سفارت>>خدمات >>روادیدوسفر>>روادید شنگن>>چک لیست های تنظیم مدارک(لینک موجود در متن صفحه)>>چه مدارکی باید ارایه کنم؟ (برگه های راهنما)
                    my_url = "https://teheran.diplo.de/ir-fa/service/visa-einreise/-/2074662"
                    #opening up connection and grabing the page
                    myPageSoup = self.scrap(my_url)
                    #grabs each 
                    container= myPageSoup.findAll("a",{"class":"rte__anchor i-pdf"})[3]["href"]
                    print("42 madarekSchengenTursist() has scraped")
                    return "https://teheran.diplo.de"+container

           
            #############################################################
           
           
            # def pasokhMosbatRavadidhayeMelli_1(self):
            #     #43
            #     # پاسخ مثپت روادیدهای ملی     
            #     #(1)
            #     # checked Address tree and title and address tree link ok!
            #     #  سایت سفارت>>خدمات >>روادیدوسفر>>روادید اقامت
            #     my_url = "https://teheran.diplo.de/ir-fa/service/visa-einreise/-/1906462"
            #     #opening up connection and grabing the page
            #     myPageSoup = self.scrap(my_url)
            #     #grabs each 
            #     container = myPageSoup.findAll("a",{"class":"rte__anchor i-pdf"})[0]["href"]
            #     print("43 zamanEhtemaliEntezarVaghtSefaratBarayeHarGrouh() has scraped")
            #     return container

            # def pasokhMosbatRavadidhayeMelli_2(self):
            #     #44
            #     # پاسخ مثپت روادیدهای ملی     
            #     #(2)
            #     # checked Address tree and title and address tree link ok!
            #     #  سایت سفارت>>خدمات >>روادیدوسفر>>روادید اقامت>>اقامت>>تحویل گرفتن روادید
            #     my_url = "https://teheran.diplo.de/ir-fa/service/visa-einreise/-/2077426"
            #     #opening up connection and grabing the page
            #     myPageSoup = self.scrap(my_url)
            #     #grabs each 
            #     container = myPageSoup.findAll("a",{"class":"rte__anchor i-pdf"})[0]["href"]
            #     print("44 zamanEhtemaliEntezarVaghtSefaratBarayeHarGrouh() has scraped")
            #     return container


