#-*- coding:utf-8 -*-
from enum import Enum

class ImgType(Enum):
    Icon = "icon"
    Promo = "promo"
    Screenshot = "screenshot"

class BuilderMaster:
    dataMaster = None

    tmp_dir = "tmp\\"
    work_dir = ""
    res_dir = ""

    apk_dir = ""
    d_eng = ""
    d_rus = ""

    data_table = ""
    default_data_file = ""

    package = ""
    name = ""

    appdf_dir = ""

    cancelbuild = false

    string[] table_values
    Dictionary<string, string> table_Dictionary

    def BuilderMaster(string dir, string package):
        dataMaster = new DataMaster()
        this.package = package
        Debug.WriteLine(package)
        name = package.Split('.')[2]

        work_dir = dir + "\\"
        res_dir = dir + "\\res_appdf\\" + name + "\\"

        if (!Directory.Exists(res_dir))
        {
            MessageBox.Show(res_dir + " not found")
            FolderBrowserDialog fbd = new FolderBrowserDialog()
            fbd.SelectedPath = dir + "\\res_appdf\\"
            DialogResult dr = fbd.ShowDialog()
            if (dr == DialogResult.OK)
            {
                DirectoryInfo di = new DirectoryInfo(fbd.SelectedPath)
                di.MoveTo(res_dir)
            }
        }

        apk_dir = work_dir + "apk\\"

        d_eng = work_dir + "full_description_eng.txt"
        d_rus = work_dir + "full_description_rus.txt"

        data_table = work_dir + "table.csv"
        default_data_file = work_dir + "appdf.txt"
        appdf_dir = work_dir + "appdf\\"

    def PrepareData():
        Directory.CreateDirectory(tmp_dir)
        foreach (string file in Directory.GetFiles(tmp_dir))
            File.Delete(file)
                   
        FileInfo fi

		#region icon
        fi = dataMaster.description.images.icon
        fi.CopyTo(tmp_dir + fi.Name)
        fi = new FileInfo(tmp_dir + fi.Name)
    
        if (!fi.Extension.Contains(".png"))
        {
            using (Image icon = Image.FromFile(fi.FullName))
            {
                icon.Save(tmp_dir + "icon.png", ImageFormat.Png)
                icon.Dispose()
            }
            fi = new FileInfo(tmp_dir + "icon.png")
        }
        ResizeImage(fi.FullName, ImgType.Icon)
        dataMaster.description.images.icon = fi
		#endregion
       
		#region promo
        fi = dataMaster.description.images.promo
        fi.CopyTo(tmp_dir + fi.Name)
        fi = new FileInfo(tmp_dir + fi.Name)
        if (!fi.Extension.Contains(".png"))
        {
            using (Image promo = Image.FromFile(fi.FullName))
            {
                promo.Save(tmp_dir + "promo.png", ImageFormat.Png)
                promo.Dispose()
            }
            fi = new FileInfo(tmp_dir + "promo.png")
        }
        ResizeImage(fi.FullName, ImgType.Promo)
        dataMaster.description.images.promo = fi
		#endregion

		#region screenshots
        List<FileInfo> screenshots = dataMaster.description.images.screenshots

        for (int i = 0 i < screenshots.Count i++ )
        {
            screenshots[i].CopyTo(tmp_dir + screenshots[i].Name)
            screenshots[i] = new FileInfo(tmp_dir + screenshots[i].Name)
            if (!screenshots[i].Extension.Contains(".png"))
            {
                try
                {
                    using (Image screen = Image.FromFile(screenshots[i].FullName))
                    {
                        screen.Save(tmp_dir + "screen_" + (i + 1).ToString() + ".png", ImageFormat.Png)
                        screen.Dispose()
                    }
                }
                catch
                {
                    cancelbuild = true
                    return
                }
                screenshots[i] = new FileInfo(tmp_dir + "screen_" + (i + 1).ToString() + ".png")
            }
            ResizeImage(screenshots[i].FullName, ImgType.Screenshot)
        }
        if (screenshots.Count == 0)
            cancelbuild = true
        else
        for (int i = screenshots.Count screenshots.Count < 4 i++)
        {
            File.Copy(screenshots[i - screenshots.Count].FullName, tmp_dir + "screen_" + (i + 1).ToString() + ".png")
            screenshots.Add(new FileInfo(tmp_dir + "screen_" + (i + 1).ToString() + ".png"))
        }

        dataMaster.description.images.screenshots = screenshots
		#endregion
    
    def FindInAppdfTXT(string key):
        value = ""
        StreamReader sr = new StreamReader(default_data_file)

        while (!sr.EndOfStream)
        {
            line = sr.ReadLine()
            if (line.IndexOf(key) == 0)
            {
                value = line.Split(new char[]{':'}, 2)[1]
                break
            }
        }
        sr.Close()
        
        return value

    def FindInTableCSV(int j):
        string[] table_keys = null
        if (table_values == null)
        {
            StreamReader sr = new StreamReader(data_table)
            table_keys = sr.ReadLine().Split('')
            while (!sr.EndOfStream)
            {
                string line = sr.ReadLine()
                if (line.Contains("" + name + ""))
                {
                    table_values = line.Split('')
                    break
                }
            }
            sr.Close()
        }
        if (table_Dictionary == null)
        {
            table_Dictionary = new Dictionary<string, string>()
            for (int i = 0 i < table_keys.Length i++)
                table_Dictionary.Add(table_keys[i], table_values[i])
        }

        return table_values[j]

    def DescriptionReplacer(string str):
        foreach (string key in from key in table_Dictionary.Keys orderby key.Length descending select key)
        {
            str = str.Replace("$" + key, table_Dictionary[key])
        }
        return str

    def CollectData():
        dataMaster.version = "1"
        dataMaster.platform = "android"
        dataMaster.package = package

        dataMaster.categorization.type = FindInAppdfTXT("type")
        dataMaster.categorization.category = FindInAppdfTXT("category")
        dataMaster.categorization.subcategory = FindInAppdfTXT("subcategory")
        if (dataMaster.categorization.subcategory == "-") 
            dataMaster.categorization.subcategory = ""
        
        dataMaster.description.texts.title = FindInTableCSV(0)
        dataMaster.description.texts.keywords = (FindInAppdfTXT("keywords").Replace("\"","") + "," + FindInTableCSV(3)).Replace(",", ", ")

        dataMaster.description.texts.full_description = DescriptionReplacer(new StreamReader(d_eng).ReadToEnd())
        dataMaster.description.texts.short_description = dataMaster.description.texts.full_description.Remove(77) + "..."

        dataMaster.description.texts.features.Add("-")
        dataMaster.description.texts.features.Add("-")
        dataMaster.description.texts.features.Add("-")
        try
        {
            dataMaster.description.images.icon = new FileInfo(Directory.GetFiles(res_dir, FindInAppdfTXT("icon_name_tamplate") + ".*")[0])
            dataMaster.description.images.promo = new FileInfo(Directory.GetFiles(res_dir, FindInAppdfTXT("big_image_template") + ".*")[0])
        }
        catch
        {
            cancelbuild = true
            return
        }
        foreach (string str in Directory.GetFiles(res_dir, FindInAppdfTXT("screenshots_name_tamplate") + "*"))
            dataMaster.description.images.screenshots.Add(new FileInfo(str))
        
        ///////////////////////////////////////////////ru///////////////////////

        Description_localization description_localization = new Description_localization()
        description_localization.texts.title = FindInTableCSV(1)
        description_localization.texts.keywords = dataMaster.description.texts.keywords

        description_localization.texts.full_description = DescriptionReplacer(new StreamReader(d_rus).ReadToEnd())
        description_localization.texts.short_description = description_localization.texts.full_description.Remove(77) + "..."
        
        description_localization.texts.features.Add("-")
        description_localization.texts.features.Add("-")
        description_localization.texts.features.Add("-")
        dataMaster.description_localizations.Add(description_localization)


        dataMaster.apk_files.apk_file = new FileInfo(apk_dir + dataMaster.description.texts.title.Replace("Memory:", "Memoria") + ".apk")
        dataMaster.customer_support.phone = FindInAppdfTXT("phone")
        dataMaster.customer_support.email = FindInAppdfTXT("email")
        dataMaster.customer_support.website = FindInAppdfTXT("website")

    def BuildDescriptionXML():        
        string description = tmp_dir + "description.xml"

        StreamWriter sw = new StreamWriter(description)
        sw.Write(dataMaster.ToXML())
        sw.Close()

    def PackFile(string sourceFile, string destFile):
        try
        {
            //Проверяем файл на существование
            if (!File.Exists(sourceFile))
                return false
            //Создаем объект для работы с архивом
            //Encoding может быть и UTF8
            using (ZipFile zip = new ZipFile(destFile, Encoding.Default))
            {
                //Устанавливаем уровень сжатия
                zip.CompressionLevel = Ionic.Zlib.CompressionLevel.Level9
                //Задаем системную директорию TEMP для временных файлов
                zip.TempFileFolder = Path.GetTempPath()
                //Добавляем файл и указываем где он будет располагаться в архиве
                //В данном случае - в корне архива
                zip.AddFile(sourceFile, "\\")
                //Сохраняем архив
                zip.Save()
            }
            return true
        }
        catch
        {
            return false
        }
    
    def BuildAppDF()
        CollectData()
        if(!cancelbuild)
            PrepareData()
        if (!cancelbuild)
            BuildDescriptionXML()
        if (cancelbuild)
            return
        Debug.WriteLine("BuildAppDF")
        
        string appdf_file = tmp_dir + package + ".appdf"
        /*
        if (!File.Exists(tmp_dir + "description.xml"))
        {
            Debug.WriteLine("no description.xml file!!!!!!!!!!!!!!!!!!!!!!!!!! skiped")
            return
        }
        if( !File.Exists(dataMaster.description.images.icon.FullName) )
        {
            Debug.WriteLine("no icon file!!!!!!!!!!!!!!!!!!!!!!!!!! skiped")
            return
        }
        if( !File.Exists(dataMaster.description.images.promo.FullName) )
        {
            Debug.WriteLine("no promo file!!!!!!!!!!!!!!!!!!!!!!!!!! skiped")
            return
        }
        if( !File.Exists(dataMaster.apk_files.apk_file.FullName))
        {
            Debug.WriteLine("no apk file!!!!!!!!!!!!!!!!!!!!!!!!!! skiped")
            return
        }
        */
        PackFile(tmp_dir + "description.xml", appdf_file)
        PackFile(dataMaster.description.images.icon.FullName, appdf_file)
        PackFile(dataMaster.description.images.promo.FullName, appdf_file)
        PackFile(dataMaster.apk_files.apk_file.FullName, appdf_file)

        foreach (FileInfo screen in dataMaster.description.images.screenshots)
            PackFile(screen.FullName, appdf_file)

        File.Copy(appdf_file, appdf_file.Replace(tmp_dir, appdf_dir))
    