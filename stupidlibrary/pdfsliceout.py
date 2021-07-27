class sandwich_extract:
    def __init__(self, col_coords, table_areas, src):
        self.col_coords = col_coords
        self.table_areas = table_areas
        
        if not (isinstance(self.col_coords,list)&isinstance(self.table_areas,list)):
            raise Exception('the given coordinates need to be list type.')
            return
        else:
            int_checker = bool([i.isdigit() for i in self.col_coords[0].split(',')])
            int_checker_1 = bool([i.isdigit() for i in self.table_areas[0].split(',')])
            
            if not (int_checker&int_checker_1):
                raise Exception('the coordinates are not purely numerical.')
                return
            else:
                pass
        try:
            import glob
            src = glob.glob(src)
            if not bool([('\\' in i)&('.pdf' in i) for i in src]):
                print('file format needs to be similar to the following example:\nr"D:\folder\...\file\**\*.pdf"')
                raise Exception('path and file format must be checked.')
                return
        except: 
            print('This package depends on the package glob: try pip install glob')
        finally:
            self.src = src
            
    def cust_observation_extract(self, out_path,up_lim_key,low_lim_key):
        if not (isinstance(out_path,str)&isinstance(up_lim_key,str)&isinstance(low_lim_key,str)):
            raise Exception("type(s) of atleast one input is not str")
            return
        with open(out_path+'\observations.txt','a') as txt:
            files = self.src  
            for file in files:
                try:
                    pdf = camelot.read_pdf(file, columns = self.col_coords ,table_areas = self.table_areas,flavor = 'stream',pages='all')
                except: 
                    raise Exception('please ensure the input file is .pdf format and camelot package is installed.')
                    break
                for page in range(pdf.n):
                    df = pdf[page].df
                    try:
                        ob_marker = pd.Index(df[df.isin([up_lim_key])].any(axis=1)).get_loc(True)
                        ob_marker2 = pd.Index(df[df.isin([low_lim_key])].any(axis=1)).get_loc(True)

                        if bool(df.iloc[ob_marker+1:ob_marker2,:][3].any()):
                            obsvn = df.iloc[ob_marker+1:ob_marker2,:][3]
                            txt.write('for \nfile : '+file+'\nfor page:'+str(page))
                            txt.write('\n')
                            txt.write('\n')
                            for i in obsvn:
                                txt.write(' '+i)
                                txt.write('\n')
                            txt.write('\n')
                            txt.write('\n')
                    except KeyError as e:

                        print(f'encountered key error : {e}\nno observation recorded for page {page} of {file}')
                        pass



        txt.close()
        
        