import datetime
from operator import methodcaller
class CaNhan():

     # thuộc tính lớp
    

     # thuộc tính đối tượng
    def __init__(self, HoTen="", NgayGiaNhap = 2021, ThoiGianHopDong = 0, LuongCoBan = 0, CMND = "", NamSinh = "", Nghe= "",hesoluong = 1):
        self.sHoTen = HoTen
        self.dNgayGiaNhap = NgayGiaNhap
        self.iThoiGianHopDong = ThoiGianHopDong
        self.dLuongCoBan = LuongCoBan
        self.sCMND = CMND
        self.iNamSinh = NamSinh
        self.sNghe = Nghe
        self.hesoluong = int(1.3)
    def __getitem__(self,key):
        return getattr(self,key)
    def Create(self, HoTen, NgayGiaNhap, ThoiGianHopDong, LuongCoBan, CMND, NamSinh):
        self.sHoTen = HoTen
        self.dNgayGiaNhap = NgayGiaNhap
        self.iThoiGianHopDong = ThoiGianHopDong
        self.dLuongCoBan = LuongCoBan
        self.sCMND = CMND
        self.iNamSinh = NamSinh
    def Nhap(self):
        print("Moi nhap Ho Ten thanh vien: ")
        self.sHoTen = input()
        print("Nhap ngay gia nhap dinh dang mm/dd/yyyy: ")
        self.dNgayGiaNhap = input()
        print("Moi nhap Thoi Gian Hop Dong: ")
        self.iThoiGianHopDong = int(input())
        print("Moi nhap Luong Co Ban cua thanh vien: ")
        self.dLuongCoBan = int(input())
        print("Moi nhap so CMND cua thanh vien: ")
        self.sCMND = input()
        print("Moi nhap Nam Sinh cua thanh vien: ")
        self.iNamSinh = int(input())

    def TinhTuoi(self):
        return 2021 - int(self.iNamSinh)

    def Xuat(self):
        print("Ho Ten thanh vien la: " + self.sHoTen)
        print("Ngay Gia Nhap: ",self.dNgayGiaNhap)
        print("Thoi gian Hop Dong cua thanh vien la: " + str(self.iThoiGianHopDong) + " nam")
        print("Luong co ban cua thanh vien la: " + str(self.dLuongCoBan) + " VND")
        print("So CMND cua thanh vien la: " + self.sCMND)
        print("Nam sinh cua thanh vien la: " + str(self.iNamSinh))
        tuoi = str(self.TinhTuoi())
        print("Tuoi cua thanh vien la: " + tuoi)

    def GiamTru(self, heso):
        GiamTruGiaCanhBanThan = 11000000
        BaoHiem = float(self.dLuongCoBan) * heso * (0.08 + 0.015 + 0.01)
        GiamTru = float(GiamTruGiaCanhBanThan) + BaoHiem
        return GiamTru

    def XacDinhBacThue(self,heso):
        ThuNhapTinhThue = float(self.dLuongCoBan) * heso - self.GiamTru(heso)
        if (ThuNhapTinhThue <= 0):
            return 0
        if (ThuNhapTinhThue <= 500 ):
            return 1
        else:
            if (ThuNhapTinhThue <= 10000000):
                return 2
            else:
                if (ThuNhapTinhThue <= 18000000):
                    return 3
                else:
                    if (ThuNhapTinhThue <= 32000000):
                        return 4
                    else:
                        if (ThuNhapTinhThue <= 52000000):
                           return 5
                        else:
                            if (ThuNhapTinhThue <= 80000000):
                                return 6
                            else:
                                return 7
    def TinhThue(self,heso):
        ThuNhapTinhThue = self.dLuongCoBan * heso - self.GiamTru(heso)
        Bac = self.XacDinhBacThue(heso)
        SoThuePhaiNop = float(0)
        if(Bac == 0):
                return 0
        else: 
            if(Bac == 1):
                SoThuePhaiNop = float(ThuNhapTinhThue) * 0.05
            else:
                if(Bac == 2):
                    SoThuePhaiNop = (float(ThuNhapTinhThue) * 0.1) - 250000
                else: 
                    if(Bac == 3):
                        SoThuePhaiNop = (float(ThuNhapTinhThue) * 0.15) - 75000
                    else:
                        if(Bac == 4):
                            SoThuePhaiNop = (float(ThuNhapTinhThue) * 0.2) - 1650000
                        else:
                            if(Bac == 5):
                                SoThuePhaiNop = (float(ThuNhapTinhThue) * 0.25) - 3250000
                            else:
                                if(Bac == 5):
                                    SoThuePhaiNop = (float(ThuNhapTinhThue) * 0.3) - 5850000
                                else:
                                    SoThuePhaiNop = (float(ThuNhapTinhThue) * 0.35) - 9850000
        return SoThuePhaiNop

    def ThoiGianHopDongConLai(self):
        res = int(self.iThoiGianHopDong) - (2021 - int(self.dNgayGiaNhap[-4:-1])*10-int(self.dNgayGiaNhap[len(self.dNgayGiaNhap)-1]))
        return res



class BacSi(CaNhan):
    def __init__(self, HoTen="", NgayGiaNhap = 2021, ThoiGianHopDong = 0, LuongCoBan = 0, CMND = "", NamSinh = "", Nghe= "BacSi",Rank= "", TruongDaoTao= ""):
        super().__init__(self,HoTen, NgayGiaNhap, ThoiGianHopDong, LuongCoBan, CMND, NamSinh, Nghe)
        self.hesoluong = float(1.15)
        self.sRank = Rank
        self.sTruongDaoTao = TruongDaoTao
        self.sNghe = Nghe

    def Nhap(self):
        print("Moi nhap thong tin Bac Si ~~ ")
        super().Nhap()
        print("Moi nhap loai bang cua Bac Si: ")
        self.sRank = input()
        print("Moi nhap truong dao tao Bac Si: ")
        self.sTruongDaoTao = input()

    def Kham(self,a):
        print("Moi nhap Tinh Trang Cau Thu: ")
        a = int(input())
        if (a < 50):
            print("Cau thu bi chan thuong !!")
            if (a < 50):
                print("Cau thu bi chan thuong !!")	                
                print("Cau thu bi chan thuong !!")
                print("1_chua tri || 2_khong chua => Your choice: ")
                temp = int(input())
                if (temp == 1):
                    a = self.ChuaBenh( a)
                    print("Cau thu da duoc chua tri !! ")
                else:
                    print("Cau thu dang chan thuong dau lam ne !! ")
        else:
            print("Cau thu dang o tinh trang the luc tot !!")
        return a
    def ChuaBenh(self,a):
        a = 100
        print("Cau thu dang o tinh trang the luc tot nhat !!")
        return a

    def TinhLuong(self):
        return float(self.dLuongCoBan) * float(self.hesoluong) - float(super().TinhThue(self.hesoluong))

    def Xuat(self):
        super().Xuat()
        print("Bang cua Bac Si hang: " + self.sRank)
        print("Truong dao tao cua Bac Si la: " + self.sTruongDaoTao)
        print("Luong cua Bac Si la: " + str(self.TinhLuong()) + " VND")
        if (self.dLuongCoBan > 11000000):
            thue = str(self.TinhThue(self.hesoluong))
            print("Thue thu nhap ca nhan cua Cau Thu la: " + str(thue) + " VND")
        else:
            print("Doi tuong khong nam trong danh sach dong thue!! ")

    def __append__(self, a):
        return a.TinhLuong(self) + a

class CauThu(CaNhan):
    def __init__(self, HoTen="", NgayGiaNhap = 2021, ThoiGianHopDong = 0, LuongCoBan = 0, CMND = "", NamSinh = "", Nghe= "CauThu",SoAo = 0, TinhTrangTheLuc = 0, TinhTrangSucKhoe = 0, ChanThuan = "trai", ViTriDaChinh= ""):
        super().__init__(self,HoTen, NgayGiaNhap, ThoiGianHopDong, LuongCoBan, CMND, NamSinh, Nghe)
        self.hesoluong = float(1.3)
        self.iSoAo = int(SoAo)
        self.iTinhTrangTheLuc = TinhTrangTheLuc
        self.iTinhTrangSucKhoe = TinhTrangSucKhoe
        self.sChanThuan = ChanThuan 
        self.sViTriDaChinh = ViTriDaChinh
        self.sNghe = Nghe

    def Create(self, HoTen, NgayGiaNhap, ThoiGianHopDong, LuongCoBan, CMND, NamSinh,SoAo, TinhTrangTheLuc, TinhTrangSucKhoe, ChanThuan, ViTriDaChinh):
        super().Create( HoTen, NgayGiaNhap, ThoiGianHopDong, LuongCoBan, CMND, NamSinh)
        self.iSoAo = int(SoAo)
        self.iTinhTrangTheLuc = TinhTrangTheLuc
        self.iTinhTrangSucKhoe = TinhTrangSucKhoe
        self.sChanThuan = ChanThuan 
        self.sViTriDaChinh = ViTriDaChinh

    def Nhap(self):
        print("Nhap Thong Tin Cau Thu ~~")
        super().Nhap()
        print("So ao cua Cau Thu la: ")
        self.iSoAo = int(input())
        print("Tinh Trang The Luc cua Cau Thu: ")
        self.iTinhTrangTheLuc = int(input())
        print("Tinh Trang Suc Khoe cua Cau Thu: ")
        self.iTinhTrangSucKhoe = int(input())
        print("Chan thuan cua Cau Thu la: ")
        self.sChanThuan = input()
        print("Vi tri Da Chinh trong doi hinh cua Cau Thu la: ")
        self.sViTriDaChinh = input()

    def TinhLuong(self):
        return float(self.dLuongCoBan) *self.hesoluong - self.TinhThue(self.hesoluong)

    def ThoiGianHopDongConLai(self):
        res = super().ThoiGianHopDongConLai()
        return res

    def Xuat(self):
        print("Thong Tin Cau Thu ~~ ")
        super().Xuat()
        print("So Ao co dinh cua Cau Thu la: " + str(self.iSoAo))
        print("Chan Thuan cua Cau Thu la: " + self.sChanThuan)
        print("Vi tri Da Chinh trong doi hinh la: " + self.sViTriDaChinh)
        print("Luong cua Cau Thu la: " + str(self.TinhLuong()) + " VND")
        if (self.dLuongCoBan > 11000000):
            print("Thue thu nhap ca nhan cua Cau Thu la: " + str(self.TinhThue(self.hesoluong)) + " VND")
        else:
            print("Doi tuong khong nam trong danh sach dong thue!! ")
        
        def __gt__(self, other): 
            if(self.iTinhTrangTheLuc>other.iTinhTrangTheLuc): 
                return True
            else: 
                return False
        def __lt__(self, other): 
            if(self.iTinhTrangSucKhoe<other.iTinhTrangSucKhoe): 
                return True
            else: 
                return False
        def __append__(self, num): 
            return self.TinhLuong() + num

class HLVChienThuat(CaNhan):
    def __init__(self, HoTen="", NgayGiaNhap = 2021, ThoiGianHopDong = 0, LuongCoBan = 0, CMND = "", NamSinh = "", Nghe= "HLVCT",Rank= 0, QuocGia= "", KinhNghiem = 0):
        super().__init__(self,HoTen, NgayGiaNhap, ThoiGianHopDong, LuongCoBan, CMND, NamSinh, Nghe)
        self.hesoluong = float(1.3)
        self.sRank = Rank
        self.sQuocGia = QuocGia
        self.iKinhNghiem = int(KinhNghiem)
        self.sNghe = Nghe

    def Nhap(self):
        print("Moi nhap thong tin HLV Chien Thuat ~~ ")
        super().Nhap()

        print("Moi nhap han cua HLV //Hang: C_B_A_Pro : ")
        self.sRank = input()

        print("Moi nhap Quoc Gia cua HLV: ")
        self.sQuocGia = input()

        print("Moi nhap so doi ma HLV da tung cong tac: ")
        self.iKinhNghiem = int(input())

    def TinhLuong(self):
        return float(self.dLuongCoBan) * self.hesoluong - self.TinhThue(self.hesoluong)

    def Xuat(self):
        super().Xuat()
        print("Hang cua HLV Chien Thuat la: " + str(self.sRank))
        print("HLV Chien Thuat den tu: " + self.sQuocGia)
        print("So doi bong HLV nay tung dan dat: " +  str(self.iKinhNghiem))
        print("Luong cua HLV Chien Thuat: " +  str(self.TinhLuong()) + " VND")
        if (self.dLuongCoBan > 11000000):
            print("Thue thu nhap ca nhan cua HLV Chien Thuat la: " + str(self.TinhThue(self.hesoluong)) + " VND")
        else:
            print("Doi tuong khong nam trong danh sach dong thue!! ")
    def ChonChienThuat(self):
        print("Ban Muon chon chien thuat nao: ")
        temp = input()
        return temp

    def __append__(self, num): 
        return self.TinhLuong() + num
class HLVTheLuc(CaNhan):
    def __init__(self, HoTen="", NgayGiaNhap = 2021, ThoiGianHopDong = 0, LuongCoBan = 0, CMND = "", NamSinh = "", Nghe= "HLVTL",ChiSoNangCaoTL = 0, NoiSinh = ""):
        super().__init__(self,HoTen, NgayGiaNhap, ThoiGianHopDong, LuongCoBan, CMND, NamSinh, Nghe)
        self.hesoluong = float(1.3)
        self.iChiSoNangCaoTL = int(ChiSoNangCaoTL)
        self.sNoiSinh = NoiSinh
        self.sNghe = Nghe

    def Nhap(self):
        print("Moi nhap thong tin HLV The Luc ~~ ")
        super().Nhap()
        print("Moi nhap chi so nang Cao TL: ")
        self.ChiSoNangCaoTL = int(input())
        print("Moi nhap Quoc Gia cua HLV The Luc: ")
        self.sNoiSinh = input()

    def TinhLuong(self):
        return self.dLuongCoBan * self.hesoluong - self.TinhThue(self.hesoluong)

    def Xuat(self):
        super().Xuat()
        print("HLV the luc den tu: " + self.sNoiSinh)
        print("chi so nang cao the luc : " + str(self.ChiSoNangCaoTL))
        print("Luong cua HLV The Luc la: " + str(self.TinhLuong()) + " VND")
        if (self.dLuongCoBan > 11000000):
            print("Thue thu nhap ca nhan cua HLV The Luc la: " + str(self.TinhThue(self.hesoluong)) + " VND")
        else:
            print("Doi tuong khong nam trong danh sach dong thue!! ")

    def __append__(self, num): 
        return self.TinhLuong() + num

class NVBaoVe(CaNhan):
    def __init__(self, HoTen="", NgayGiaNhap = 2021, ThoiGianHopDong = 0, LuongCoBan = 0, CMND = "", NamSinh = "", Nghe= "BaoVe",ThoiGianLamTrongNgay = 0, MauDongPhuc = ""):
        super().__init__(self,HoTen, NgayGiaNhap, ThoiGianHopDong, LuongCoBan, CMND, NamSinh, Nghe)
        self.hesoluong = float(1.0)
        self.iThoiGianLamTrongNgay = int(ThoiGianLamTrongNgay)
        self.sMauDongPhuc = MauDongPhuc
        self.sNghe = Nghe

    def Nhap(self):
        print("Moi nhap thong tin Nhan Vien Bao Ve ~~ ")
        super().Nhap()

        print("Moi nhap Thoi Gian Lam Viec/Ngay cua Nhan Vien Bao Ve: ")
        self.iThoiGianLamTrongNgay = int(input())

        print("Moi nhap Mau Dong Phuc hom nay cu Nhan Vien Bao Ve: ")
        self.sMauDongPhuc = input()

    def TinhLuong(self):
        return self.dLuongCoBan
    #NVBaoVe luong < 11tr => ko phai doi tuong nop thue
    def Xuat(self):
        super().Xuat()
        print("Tong thoi gian lam tren mot ngay la: " + str(self.iThoiGianLamTrongNgay))
        print("Mau Dong Phuc NV Bao Ve: " + self.sMauDongPhuc)

    def __append__(self, num): 
        return self.TinhLuong() + num
class NVVeSinh(CaNhan):
    def __init__(self, HoTen="", NgayGiaNhap = 2021, ThoiGianHopDong = 0, LuongCoBan = 0, CMND = "", NamSinh = "", Nghe= "VeSinh",Shift = 0, Thuong = 0):
        super().__init__(self,HoTen, NgayGiaNhap, ThoiGianHopDong, LuongCoBan, CMND, NamSinh, Nghe)
        self.hesoluong = float(1.0)
        self.iShift = int(Shift)
        self.dThuong = float(Thuong)
        self.sNghe = Nghe

    def Nhap(self):
        print("Moi nhap thong tin Nhan Vien Ve Sinh ~~ ")
        super().Nhap()
        print("Moi nhap Ca lam viec cua Nhan Vien Ve Sinh: ")
        self.iShift = int(input())
        print("Moi nhap Luong thuong cua Nhan Vien Ve Sinh: ")
        self.dThuong = float(input())

    def TinhLuong(self):
        return self.dLuongCoBan + self.dThuong

    #NVVeSinh luong < 11tr => ko phai doi tuong nop thu

    def Xuat(self):
        super().Xuat()
        print("Ca lam cua Nhan Vien Ve Sinh la: " + str(self.iShift))
        print("Luong thuong them cua Nhan Vien Ve Sinh la: " + str(self.dThuong) + " VND")

    def __append__(self, num): 
        return self.TinhLuong() + num
class San:
    def __init__(self, TenSan= "", SoLuongKhanGia = 0, GiaVe=0):
        self.sTenSan = TenSan
        self.iSoLuongKhanGia = SoLuongKhanGia
        self.dGiaVe = GiaVe

    def Nhap(self):
        print("Moi nhap Ten San: ")
        self.sTenSan = input()
        print("Moi nhap Gia ve vao san: ")
        self.dGiaVe = float(input())
        print("Moi nhap So Luong Khan Gia ma San chua duoc toi da: ")
        self.iSoLuongKhanGia = int(input())
    def Xuat(self):
        print("Ten San Van Dong cua Doi Bong la: " + self.sTenSan)
        print("Gia ve vao san la: " + str(self.dGiaVe))
        print("So luong Khan Gia khan dai co the chua duoc la: " + str(self.iSoLuongKhanGia))

class QuanLyCauThu:
    def __init__(self, DsCauThu = list()):
        self.lDsCauThu = DsCauThu

    def Nhap(self):
        print("Moi nhap so luong cau thu trong doi bong: ")
        cauthu = int(input())
        for i in range(cauthu):
            a = CauThu()
            a.Nhap()
            self.lDsCauThu.append(a)

    def Xuat(self):
        print("So luong cau thu trong doi bong la: " + str(len(self.lDsCauThu)))
        for item in self.lDsCauThu:
            item.Xuat()

    def myFunc1(self,e):
        return e['sHoTen']
    def myFunc2(self,e):
        return e.TinhTuoi()
    def myFunc3(self,e):
        return e['dNgayGiaNhap']
    def myFunc4(self,e):
        return e.ThoiGianHopDongConLai()
    def myFunc5(self,e):
        return e['iSoAo']
    def myFunc6(self,e):
        return e['iTinhTrangTheLuc']
    def myFunc7(self,e):
        return e['iTinhTrangSucKhoe']

    def Sort(self):
        print("\t\t\t************************MENU************************\t\t\t")
        print("\t\t\t***              1. Ho ten                       ***\t\t\t")
        print("\t\t\t***              2. Tuoi                         ***\t\t\t")
        print("\t\t\t***              3. Ngay gia nhap                ***\t\t\t")
        print("\t\t\t***              4. Thoi han hop dong con lai    ***\t\t\t")
        print("\t\t\t***              5. So ao                        ***\t\t\t")
        print("\t\t\t***              6. TT the luc                   ***\t\t\t")
        print("\t\t\t***              7. TT Suc Khoe                  ***\t\t\t")
        print("\t\t\t****************************************************\t\t\t")
        print("Moi nhap lua chon cua ban => Your choice: ")
        choice = int(input())
        if( choice == 1):
            self.lDsCauThu.sort(key = self.myFunc1)
        if(choice == 2):
            self.lDsCauThu = sorted(self.lDsCauThu,key = lambda Obj:Obj.TinhTuoi())
        if(choice == 3):
            self.lDsCauThu.sort(key = self.myFunc3)   
        if(choice == 4):
            self.lDsCauThu = sorted(self.lDsCauThu,key = lambda Obj:Obj.ThoiGianHopDongConLai())
        if(choice == 5):
            self.lDsCauThu.sort(key = self.myFunc5)
        if(choice == 6):
            self.lDsCauThu.sort(key = self.myFunc6)
        if(choice == 7):
            self.lDsCauThu.sort(key = self.myFunc7)

    def Loc(self):
        temp = list()
        print("\t\t\t************************MENU************************\t\t\t")
        print("\t\t\t***       1. Danh sach cau thu thuan chan trai   ***\t\t\t")
        print("\t\t\t***       2. Danh sach cau thu thuan chan phai   ***\t\t\t")
        print("\t\t\t***       3. Danh sach cau thu co the da tien dao***\t\t\t")
        print("\t\t\t***       4. Danh sach cau thu co the da tien ve ***\t\t\t")
        print("\t\t\t***       5. Danh sach cau thu co the da hau ve  ***\t\t\t")
        print("\t\t\t***       6. Thoat                               ***\t\t\t")
        print("\t\t\t****************************************************\t\t\t")
        print("Moi nhap lua chon cua ban => Your choice: ")
        choice = int(input())
        if(choice == 1):
            for item in self.lDsCauThu:
                if (item.sChanThuan == "trai"):
                    temp.append(item)
        if(choice == 2):
            for item in self.lDsCauThu:
                if (item.sChanThuan == "phai"):
                    temp.append(item)
        if(choice == 3):
            for item in self.lDsCauThu:
                if (item.sViTriDaChinh == "tiendao"):
                    temp.append(item)
        if(choice == 4):
            for item in self.lDsCauThu:
                if (item.sViTriDaChinh == "trungve"):
                    temp.append(item)
        if(choice == 5):
            for item in self.lDsCauThu:
                if (item.sViTriDaChinh == "hauve"):
                        temp.append(item)
        return temp
        
    def Search(self):
        print("\t\t\t************************MENU************************\t\t\t")
        print("\t\t\t***            1. Ho ten                         ***\t\t\t")
        print("\t\t\t***            2. So ao                          ***\t\t\t")
        print("\t\t\t***            3. Thoat                          ***\t\t\t")
        print("\t\t\t****************************************************\t\t\t")
        print("Moi nhap lua chon cua ban => Your choice: ")
        choice = int(input())
        temp = None
        if(choice == 1):
            print("Nhap ten cau thu tim kiem : ")
            key = input()
            for i in self.lDsCauThu:
                if (i.sHoTen == key):
                    temp = i
            return temp
        if(choice == 2):
            print("Nhap so ao cau thu tim kiem : ")
            key = int(input())
            for i in self.lDsCauThu:
                if (int(i.iSoAo) == key):
                    temp = i
            return temp
        if(choice == 3):
                return None

    def XemtinhTrangtheLuc(self):
        for item in self.lDsCauThu:
            print("Cau thu " + item.sHoTen + " chi so TL la: " + str(item.iTinhTrangTheLuc))

    def XemtinhTrangSucKhoe(self):
        for item in self.lDsCauThu:
            print("Cau thu " + item.sHoTen + " chi so SK la: " + str(item.iTinhTrangSucKhoe))

    def CauThuCoTheLucTotNhat(self):
        if (len(self.lDsCauThu) == 0):
            return None
        else:
            temp = self.lDsCauThu[0]
            for item in self.lDsCauThu:
                if (item.iTinhTrangTheLuc> temp.iTinhTrangTheLuc):
                    temp = item
            return temp

    def CauThuCoTheSucKhoeYeuNhat(self):
        if (len(self.lDsCauThu) == 0):
            return None
        else:
            temp = self.lDsCauThu[0]
            for item in self.lDsCauThu:
                if (item.iTinhTrangSucKhoe < temp.iTinhTrangSucKhoe):
                    temp = item
            return temp

    def TongLuongToanCauThu(self):
        temp = 0
        for item in self.lDsCauThu:
            temp = item.TinhLuong() + temp
        return temp

    def xoaCT(self):
        print("So luong cau thu hien tai la: " + len(self.lDsCauThu))
        print("Ban muon xoa bao nhieu Cau thu: ")
        n = int(input())
        for i in range(n):
            print("Danh sach cau thu: ")
            for item in self.lDsCauThu:
                print("Ten Cau Thu: " + item.sHoTen)
            print("Nhap thu tu Cau thu muon xoa: ")
            x = Parse(input())
            self.xoa1CT(x)
    def xoa1CT(self, x):
        self.lDsCauThu.pop(x)

class QuanLyNhanVien:
    def __init__(self, caNhans = list(),bacsi = list(),HLVCT = list(),HLVTL = list(),NVVS = list(),NVBV = list()):
        self.lcaNhans = caNhans
        self.lbacsi = bacsi
        self.lHLVCT = HLVCT
        self.lHLVTL = HLVTL
        self.lNVBV = NVBV
        self.lNVVS = NVVS


    def TinhLuongToanBoNV(self):
        temp = float(0)
        for item in self.lbacsi:
            temp = float(item.TinhLuong()) + float(temp)
        for item in self.lHLVCT:
            temp = float(item.TinhLuong()) + float(temp)
        for item in self.lHLVTL:
            temp = float(item.TinhLuong()) + float(temp)
        for item in self.lNVBV:
            temp = float(item.TinhLuong()) + float(temp)
        for item in self.lNVVS:
            temp = float(item.TinhLuong()) + float(temp)
        return temp

    def Nhap(self):
        print("Moi nhap so luong Bac Si: ")
        bs = int(input())
        for i in range(bs):
            a =  BacSi()
            a.Nhap()
            self.lbacsi.append(a)
            self.lcaNhans.append(a)
        print("Moi nhap so luong HLV Chien Thuat: ")
        hlvct = int(input())
        for  i in range(hlvct):
            a =  HLVChienThuat()
            a.Nhap()
            self.lHLVCT.append(a)
            self.lcaNhans.append(a)
        

        print("Moi nhap so luong HLV The Luc: ")
        hlvtl = int(input())
        for  i in range(hlvtl):
            a =  HLVTheLuc()
            a.Nhap()
            self.lcaNhans.append(a)
            self.lHLVTL.append(a)
        

        print("Moi nhap so luong Nhan Vien Bao Ve: ")
        nvbv = int(input())
        for  i in range(nvbv):
            a =  NVBaoVe()
            a.Nhap()
            self.lNVBV.append(a)
            self.lcaNhans.append(a)
        

        print("Moi nhap so luong Nhan Vien Ve Sinh: ")
        nvvs = int(input())
        for  i in range(nvvs):
            a =  NVVeSinh()
            a.Nhap()
            self.lNVVS.append(a)
            self.lcaNhans.append(a)
        
    

    def Sort(self):
        self.lcaNhans = sorted(self.lcaNhans,key = lambda Obj:Obj.dLuongCoBan)


    def XuatDsBacSi(self):
        if (len(self.lbacsi) == 0):
            print("Khong co Bac Si nao!")
        else:
            for item in self.lbacsi:
                print("Ten: " + item.sHoTen + " Chuc vu: " + item.sNghe)

    def chonBacsi(self):
        self.XuatDsBacSi()
        if(len(self.lbacsi) != 0):
            print("Ban muon chon bac si so may: ")
            key = int(input())
            return self.lbacsi[key]
        return None


    def XuatDsHLVTL(self):
        if (len(self.lHLVTL) == 0):
            print("Khong co HLV the luc nao!")
        else:
            for item in self.lHLVTL:
                print("Ten: " + item.sHoTen + " Chuc vu: " + item.sNghe)

    def chonHLVCT(self):
        self.XuatDsHLVCT()
        print("Ban muon chon bac si so may: ")
        key = int(input())
        return self.lHLVCT[key]

    def XuatDsHLVCT(self):
        if (len(self.lHLVCT) == 0):
            print("Khong co HLV chien thuat nao!")
        else:
            for item in self.lHLVCT:
                print("Ten: " + item.sHoTen + " Chuc vu: " + item.sNghe)


    def XuatDsNVBV(self):
        if (len(self.lNVBV) == 0):
            print("Khong co nhan vien bao ve nao!")
        else:
            for item in self.lNVBV:
        
                print("Ten: " + item.sHoTen + "Chuc vu: "  + item.sNghe)
        
    def XuatDsNVVS(self):
        if (len(self.lNVVS) == 0):
            print("Khong co nhan vien ve sinh nao!")
        else:
            for item in self.lNVVS:
                print("Ten: " + item.sHoTen + " Chuc vu: " + item.sNghe)

    def Xuat(self):
        if (len(self.lcaNhans) == 0):
            print("Khong co nhan vien nao!")
        else:
            for item in self.lcaNhans:
                print("Ten: " + item.sHoTen + " Chuc vu: " + item.sNghe)


    def Search(self):
        print("Nhap ten Nhan Vien muon tim kiem : ")
        key = input()
        temp = CaNhan()
        for item in self.lcaNhans:
               if(item.sHoTen == key):
                    temp = item
        return temp
    def Search(self,key):
        temp = CaNhan()
        for item in self.lcaNhans:
               if(item.sHoTen == key):
                    temp = item
        return temp

    def Loc(self):
        print("\t\t\t************************MENU************************\t\t\t")
        print("\t\t\t***            1. Loc theo Luong > x             ***\t\t\t")
        print("\t\t\t***            2. Loc theo Luong < x             ***\t\t\t")
        print("\t\t\t***            3. Thoat                          ***\t\t\t")
        print("\t\t\t****************************************************\t\t\t")
        print("Moi nhap lua chon cua ban => Your choice: ")
        choice = int(input())
        temp = CauThu()
        if(choice == 1):
                return LocTheoLuongLon()
        if(choice == 2):
                return LocTheoLuongBe()
        if(choice == 3):
                return None

    def LocTheoLuongLon(self):
        print("Nhap Luong (x) de co danh sach cau thu luong > x: ")
        x = int(input())
        temp =  list()
        for item in self.lcaNhans:
            if (item.dLuongCoBan > x):
                temp.append(item)
        return temp


    def LocTheoLuongBe(self):
        print("Nhap Luong (x) de co danh sach cau thu luong < x: ")
        x = int(input())
        temp =  list()
        for item in self.lcaNhans:
            if(item.dLuongCoBan < x):
                temp.append(item)
        return temp


    def XemcaNhan(self):
        self.Xuat()
        print("Ban Muon Xem Nhan Vien thu may: !")
        x = int(input())
        self.lcaNhans[x].Xuat()
    def xoaNV():
        print("So luong nhan vien hien tai la: " + str(len(self.lcaNhans)))
        print("Ban muon xoa bao nhieu NV: ")
        n = int(input())
        temp.Xuat()            
        for i in range(n):
            print("Danh sach nhan vien: ")
            for item in self.lcaNhans:
                print("Ho ten: " + item.sHoTen + " Chuc vu: " + item.sNghe)
            print("Nhap thu tu NV muon xoa: ")
            x = int(input())
            self.xoa1NV(x)
    def xoa1NV(x):
        temp = self.lcaNhans[x]
        if (temp.sNghe == "bacsi"):
            for temp1 in self.listNhanVien.lBacSi:
                    if(temp1.sHoTen == temp.sHoTen):
                        self.listNhanVien.lBacSi.remove(temp1)
        if (temp.sNghe == "HLVCT"):
            for temp1 in self.listNhanVien.lHLVCT:
                if(temp1.sHoTen == temp.sHoTen):
                    if(temp1.sHoTen == temp.sHoTen):
                        self.listNhanVien.lHLVCT.remove(temp1)
        if (temp.sNghe == "HLVTL"):
            for temp1 in self.listNhanVien.lHLVTL:
                if(temp1.sHoTen == temp.sHoTen):
                        self.listNhanVien.lHLVTL.remove(temp1)
        if (temp.sNghe == "NVVeSinh"):
            for temp1 in self.listNhanVien.lNVVS:
                if(temp1.sHoTen == temp.sHoTen):
                        self.listNhanVien.lNVVS.remove(temp1)
        if (temp.sNghe == "NVBaoVe"):
            for temp1 in self.listNhanVien.lNVBV:
                if(temp1.sHoTen == temp.sHoTen):
                        self.listNhanVien.lNVBV.remove(temp1)
        self.lcaNhans.RemoveAt(temp)
class DoiBong:
    def __init__(self, TenDoiBong = "",TenNhaTaiTro = "",san = San(),CauThus = QuanLyCauThu(),Nhanviens = QuanLyNhanVien(), expi = list()):
        self.sTenDoiBong = TenDoiBong
        self.sTenNhaTaiTro = TenNhaTaiTro
        self.sanDoiBong = san
        self.listCauThu = CauThus
        self.listNhanVien= Nhanviens
        self.expired = expi
   
    def Xuat(self):
        print("Ten Doi Bong la: " + self.sTenDoiBong)
        print("Ten Nha Tai Tro cua Doi Bong la: " + self.sTenNhaTaiTro)
    
    def Nhap(self):
        print("Moi nhap Ten Doi Bong: ")
        self.sTenDoiBong = input()
        print("Ten Nha Tai Tro cua Doi Bong: ")
        self.sTenNhaTaiTro = input()

    def MenuQLCT(self):
        flag = 1
        while (flag == 1):
            print("\t\t\t************************MENU************************\t\t\t")
            print("\t\t\t***      0. Nhap cau thu                         ***\t\t\t")
            print("\t\t\t***      1. Sap xep Cau Thu                      ***\t\t\t")
            print("\t\t\t***      2. Loc Cau Thu                          ***\t\t\t")
            print("\t\t\t***      3. Tim Kiem Cau Thu                     ***\t\t\t")
            print("\t\t\t***      4. Xem Tinh Trang The Luc cua Cau Thu   ***\t\t\t")
            print("\t\t\t***      5. Xem Tinh Trang Suc Khoe cua Cau Thu  ***\t\t\t")
            print("\t\t\t***      6. Cau Thu co The Luc Tot Nhat          ***\t\t\t")
            print("\t\t\t***      7. Cau Thu co Suc Khoe Yeu Nhat         ***\t\t\t")
            print("\t\t\t***      8. Tong Luong Cau Thu                   ***\t\t\t")
            print("\t\t\t***      9. Thoat                                ***\t\t\t")
            print("\t\t\t****************************************************\t\t\t")
            ("Moi nhap lua chon cua ban => Your choice: ")
            choice = int(input())
            if( choice == 0):
                    self.listCauThu.Nhap()
            if( choice == 1):
                    self.listCauThu.Sort()
                    self.listCauThu.Xuat()
            if( choice == 2):
                    temp = self.listCauThu.Loc()
                    for item in temp:
                        item.Xuat()
            if( choice == 3):
                    temp = self.listCauThu.Search()
                    if (temp == None):
                        print("Khong tim thay cau thu")
                    else:
                        temp.Xuat()
            if( choice == 4):
                    self.listCauThu.XemtinhTrangtheLuc()
            if( choice == 5):
                    self.listCauThu.XemtinhTrangSucKhoe()
            if( choice == 6):
                    temp=self.listCauThu.CauThuCoTheLucTotNhat()
                    if (temp == None):
                        print("Khong tim thay cau thu")
                    else:
                        temp.Xuat()
            if( choice == 7):
                    temp = self.listCauThu.CauThuCoTheSucKhoeYeuNhat()
                    if (temp == None):
                        print("Khong tim thay cau thu")
                    else:
                        temp.Xuat()
            if( choice == 8):
                    print("Tong luong phai tra cho cac Cau  Thu la: " + str(self.listCauThu.TongLuongToanCauThu()))
            if( choice == 9):
                    flag = 0
    def MenuQLNV(self):
        flag = 1
        while (flag == 1):
            print("\t\t\t************************MENU************************\t\t\t")
            print("\t\t\t***      0. Nhap NV                              ***\t\t\t")
            print("\t\t\t***      1. Sap xep Nhan Vien theo Luong         ***\t\t\t")
            print("\t\t\t***      2. Loc Nhan Vien theo Luong lon         ***\t\t\t")
            print("\t\t\t***      3. Loc Nhan Vien theo Luong be          ***\t\t\t")
            print("\t\t\t***      4. Xem Danh Sach Bac Si                 ***\t\t\t")
            print("\t\t\t***      5. Xem Danh Sach HLV Chien Thuat        ***\t\t\t")
            print("\t\t\t***      6. Xem Danh Sach HLV The Luc            ***\t\t\t")
            print("\t\t\t***      7. Xem Danh Sach Nhan Vien Bao Ve       ***\t\t\t")
            print("\t\t\t***      8. Xem Danh Sach Nhan Vien Ve Sinh      ***\t\t\t")
            print("\t\t\t***      9. Tong Luong Nhan Vien                 ***\t\t\t")
            print("\t\t\t***     10. Thoat                                ***\t\t\t")
            print("\t\t\t****************************************************\t\t\t")
            ("Moi nhap lua chon cua ban => Your choice: ")
            choice = int(input())
            if( choice == 0):
                    self.listNhanVien.Nhap()
            if( choice == 1):
                    self.listNhanVien.Sort()
                    self.listNhanVien.Xuat()              
            if( choice == 2):
                    temp = self.listNhanVien.LocTheoLuongLon()
                    print("Danh sach Nhan Vien co Luong lon hon x da nhap: ")
                    for item in temp:
                        item.Xuat()
                        print()
            if( choice == 3):       
                    temp = self.listNhanVien.LocTheoLuongBe()
                    print("Danh sach Nhan Vien co Luong be hon x da nhap: ")
                    for item in temp:
                        item.Xuat()
                        print()
            if( choice == 4):
                    self.listNhanVien.XuatDsBacSi()
            if( choice == 5):
                    self.listNhanVien.XuatDsHLVCT()  
            if( choice == 6):
                    self.listNhanVien.XuatDsHLVTL()
            if( choice == 7):
                    self.listNhanVien.XuatDsNVBV()
            if( choice == 8):
                    self.listNhanVien.XuatDsNVVS()
            if( choice == 9):
                    print("Tong luong toan nhan vien la: " + str(self.listNhanVien.TinhLuongToanBoNV()))
            if( choice == 10):
                    flag = 0
           
    def MenuHoatDong(self):
        flag = 1
        tmp = list()
        tmp = HoatDong.createCauThu(tmp)
        while (flag == 1):
            print("\t\t\t************************MENU************************\t\t\t")
            print("\t\t\t***      1. Kham Suc Khoe Toan Doi               ***\t\t\t")
            print("\t\t\t***      2. Kham Suc Khoe Cau Thu                ***\t\t\t")
            print("\t\t\t***      3. Chon Doi 11 Nguoi                    ***\t\t\t")
            print("\t\t\t***      4. Huan Luyen The Luc Ca Doi            ***\t\t\t")
            print("\t\t\t***      5. Huan Luyen The Luc Cau Thu           ***\t\t\t")
            print("\t\t\t***      6. Da thu                               ***\t\t\t")
            print("\t\t\t***      7. Thao tac hop dong                    ***\t\t\t")
            print("\t\t\t***      8. Chuyen Nhuong                        ***\t\t\t")
            print("\t\t\t***      9. Thoat                                ***\t\t\t")
            print("\t\t\t****************************************************\t\t\t")
            print("Moi nhap lua chon cua ban => Your choice: ")
            choice = int(input())
            BsKham= BacSi()
            if(choice == 1):
                BsKham = self.listNhanVien.chonBacsi()
                if (BsKham != None):
                    self.listCauThu.lDsCauThu = HoatDong.KhamSucKhoeToanDoi(self.listCauThu.lDsCauThu, BsKham)
                    self.listCauThu.XemtinhTrangSucKhoe()
            if( choice == 2):
                BsKham = self.listNhanVien.chonBacsi()
                if (BsKham != None):
                    for item in self.listCauThu.lDsCauThu:
                        print("Ten: " + item.sHoTen + " So Ao: " + str(item.iSoAo))
                    print("Muon Kham Suc Khoe Cau Thu thu: ")
                    i = int(input())
                    temp =  self.listCauThu.lDsCauThu[i]   
                    temp = HoatDong.KhamSucKhoeCauThu(temp, BsKham)
                    self.listCauThu.lDsCauThu[i] = temp
                    self.listCauThu.XemtinhTrangSucKhoe()   
            if( choice == 3):
                    temp = HoatDong.TuyenChon11CT(self.listCauThu.lDsCauThu)
                    print("Doi Hinh da lua chon: ")
                    for item in temp:
                        print("Ten: " + item.sHoTen + " Vi Tri: " + str(item.sViTriDaChinh))
            if( choice == 4):
                    temp = HoatDong.HuanLuyenTLCaDoi(self.listCauThu.lDsCauThu, self.listNhanVien.lHLVTL[0])
                    self.listCauThu.lDsCauThu = temp
                    self.listCauThu.XemtinhTrangtheLuc()       
            if( choice == 5):
                    for item in self.listCauThu.lDsCauThu:
                        print("Ten: " + item.sHoTen + " CMND: " + item.sCMND)
                    ("Muon Cai Thien The Luc Cau Thu thu: ")
                    i = int(input())
                    temp = self.listCauThu.lDsCauThu[i]
                    self.listCauThu.lDsCauThu[i]=HoatDong.HuanLuyenTL(temp, self.listNhanVien.lHLVTL[0])
                    self.listCauThu.XemtinhTrangtheLuc()
            if( choice == 6):
                    if (len(self.listCauThu.lDsCauThu) < 11):
                        print("Khong du cau thu de tham gia thi dau")
                    if (len(self.listNhanVien.lHLVCT) == 0):
                        print("Khong co HLV")
                    hlv = self.listNhanVien.chonHLVCT()
                    HoatDong.DaGiaoLuu(self.listCauThu.lDsCauThu, hlv)
            if( choice == 7):
                    self.ThaoTacHopDong()
                    self.expired.clear()
            if( choice == 8):
                    HoatDong.ChuyenNhuong(self.listCauThu,tmp)
            if( choice == 9):
                    flag = 0 
    def ThaoTacHopDong(self):
        self.DanhSachHetHanHopDong()
        if (len(self.expired) <= 0):
            print("Khong co nhan vien nao het han hop dong !!")
        else:
            flag = 1
            while (flag == 1):
                dem = 0
                print("Danh sach het han hop dong la: ")
                for item in self.expired:
                    print("STT: " + str(dem) + "Ho ten: " + item.sHoTen + " Luong: ")
                    dem= dem+1
                print("1_Gia Han || 2_Kick => Your choice: ")
                n = int(input())
                if(n == 1):       
                    print("Ban muon gia han nhan vien thu may: ")
                    x = int(input())
                    if (self.expired[x].sNghe == "CauThu"):   
                        for item in self.listCauThu.lDsCauThu:
                            if (item.sHoTen == self.expired[x].sHoTen):           
                                print("Gia han hop dong bao nhieu nam?: ")
                                item.iThoiGianHopDong = int(input())
                                item.dNgayGiaNhap = 2021
                                self.expired.remove(self.expired[x])
                                break
                    else:
                        for item in self.listNhanVien.lcaNhans:
                            if (item.sHoTen == self.expired[x].sHoTen):
                                print("Gia han hop dong bao nhieu nam?: "+item.sHoTen+" "+ str(x))
                                temp = int(input())
                                item.iThoiGianHopDong = temp
                                item.dNgayGiaNhap = 2021
                                if (self.expired[x].sNghe == "bacsi"):
                                    for temp1 in self.listNhanVien.lBacSi:
                                        if(temp1.sHoTen == self.expired[x].sHoTen):
                                            temp1.iThoiGianHopDong = temp
                                            temp1.dNgayGiaNhap = 2021
                                if (self.expired[x].sNghe == "HLVCT"):
                                    for temp1 in self.listNhanVien.lHLVCT:
                                        if(temp1.sHoTen == self.expired[x].sHoTen):
                                            temp1.iThoiGianHopDong = temp
                                            temp1.dNgayGiaNhap = 2021
                                if (self.expired[x].sNghe == "HLVTL"):
                                    for temp1 in self.listNhanVien.lHLVTL:
                                            if(temp1.sHoTen == self.expired[x].sHoTen):
                                                temp1.iThoiGianHopDong = temp
                                                temp1.dNgayGiaNhap = 2021  
                                if (self.expired[x].sNghe == "NVVeSinh"):
                                    for temp1 in self.listNhanVien.lNVVS:
                                            if(temp1.sHoTen == self.expired[x].sHoTen):
                                                temp1.iThoiGianHopDong = temp
                                                temp1.dNgayGiaNhap = 2021
                                if (self.expired[x].sNghe == "NVBao"):
                                    for temp1 in self.listNhanVien.lNVBV:
                                                if(temp1.sHoTen == self.expired[x].sHoTen):
                                                    temp1.iThoiGianHopDong = temp
                                                    temp1.dNgayGiaNhap = 2021
                                self.expired.remove(self.expired[x])
                                break
                if(n == 2):
                        print("Ban muon kick nhan vien thu may: ")
                        x = int(input())
                        if (self.expired[x].sNghe != "CauThu"):
                            temp = 0
                            for i,item in enumerate(self.listNhanVien.lcaNhans):
                                if (item.sHoTen == self.expired[x].sHoTen):
                                    temp = i
                            self.listNhanVien.xoa1NV(temp)
                            self.expired.remove(self.expired[x])
                        else:
                            temp = 0
                            for i,item in enumerate(self.listCauThu.lDsCauThu):
                                if (item.sHoTen == self.expired[x].sHoTen):
                                    temp = i
                            self.listCauThu.xoa1CT(temp)
                            self.expired.remove(self.expired[x])   
            print("1_ De tiep tuc !! => Your choice: ")
            flag = int(input())
    def DanhSachHetHanHopDong(self):
        for item in self.listCauThu.lDsCauThu:
            if(item.ThoiGianHopDongConLai() <= 0):
                self.expired.append(item)
        for item in self.listNhanVien.lcaNhans:
            if (item.ThoiGianHopDongConLai() <= 0):
                self.expired.append(item)
class HoatDong:
    def KhamSucKhoeToanDoi(List1, BS):
        for i in List1:
            i = HoatDong.KhamSucKhoeCauThu(i,BS)
        return List1
    def KhamSucKhoeCauThu(CT, BS):
        a = 0
        print("Cau thu: " + CT.sHoTen)
        a = BS.Kham(a)
        CT.iTinhTrangSucKhoe = a
        return CT
    def TuyenChon11CT(lDsCauThu):
        temp=list()
        print("=============================")
        print(" 1: Chon 11 Cau thu co TL tot nhat")
        print(" 2: Tu ban chon")
        print("Ban muon chon theo cai gi: ")
        choice = int(input())
        if(choice == 1):
            if(len(lDsCauThu)<=11):
                print("Doi <=11 nguoi => Khong the chon Doi !!")
                return lDsCauThu
            else:
                lDsCauThu = sorted(lDsCauThu,key = lambda Obj:Obj.sHoTen)
                for i in lDsCauThu:
                    temp.append(i)
                return temp
        else:
            print("Day la DS cau thu")
            for item in lDsCauThu:
                print(" " + item.sHoTen)
            for i in range(11):
                print("Moi chon cau thu thu " + str((i + 1)) + ": ")
                x= int(input())
                temp.append(lDsCauThu[x])
            return temp

    def HuanLuyenTLCaDoi(List, HLV):
        for i in List:
            i.iTinhTrangTheLuc += 4
        return List
 
    def HuanLuyenTL(CT, HLV):
        CT.iTinhTrangTheLuc += 5
        print( HLV.iChiSoNangCaoTL)
        return CT
    def DaGiaoLuu(listCT, HLV):
        print("Chon cau thu tham gia thi dau")
        listCT2=HoatDong.TuyenChon11CT(listCT)
        print("Chon chien thuat")
        chienthuat = HLV.ChonChienThuat()
        print("Nhap doi thu: ")
        dt = input()
        print("\t\t\t************************************************\t\t\t")
        print("Doi nha VS" + dt)
        print("Danh sach cau thu tham du!")
        for item in listCT2:
            print("Cau thu " + item.sHoTen + " so ao: " + str(item.iSoAo))
        print("Huan luyen vien: "+HLV.sHoTen)
        print("Chien thuat: " + chienthuat)
        print("\t\t\t************************************************\t\t\t")
    
    def createCauThu(tmp):
        a = CauThu()
        b = CauThu()
        c = CauThu()
        d = CauThu()
        e = CauThu()
        f = CauThu()
        a.Create("nguyen van a", 1998, 1, 30000000, "56893457",2001,12, 56, 72, "trai", "tienve")
        b.Create("nguyen van b", 2005, 2, 20000000, "56630787", 2000, 90, 88, 12, "phai", "hauve")
        c.Create("nguyen van c", 2007, 4, 67000000, "99637457", 1995, 57, 26, 82, "trai", "tiendao")
        d.Create("nguyen van d", 2009, 11, 100000000, "63019457", 1998, 420, 100, 100, "phai", "tiendao")
        e.Create("nguyen van e", 2012, 9, 12000000, "56891234", 2005, 1, 36, 22, "phai", "tiendao")
        f.Create("nguyen van f", 2020, 7,10000000, "12343457", 2004, 1, 46, 52, "phai", "tienve")
        a.Xuat()
        chuyennhuong = list()
        chuyennhuong.append(a)
        chuyennhuong.append(b)
        chuyennhuong.append(c)
        chuyennhuong.append(d)
        chuyennhuong.append(e)
        chuyennhuong.append(f)
        tmp = chuyennhuong
        return chuyennhuong

    def ChuyenNhuong( qlct,temp):
        print("Da den ki chuyen nhuong mua Dong, ban co muon mua them hay ban di cau thu ko? 1_Yes || 2_No")
        print("=> Your choice: ")
        choice = int(input())
        if (choice == 1):
            flag = 1
            while (flag == 1):
                print("\t\t\t************************MENU************************\t\t\t")
                print("\t\t\t***            1. Mua                            ***\t\t\t")
                print("\t\t\t***            2. Ban                            ***\t\t\t")
                print("\t\t\t***            3. Thoat                          ***\t\t\t")
                print("\t\t\t****************************************************\t\t\t")
                print("Moi nhap lua chon cua ban => Your choice: ")
                choice1 = int(input())
                if(choice1 == 1):
                    i = 0
                    for item in temp:
                        print("STT: " + str(i) + " Ho ten: " + str(item.sHoTen) + " Luong: " + str(item.dLuongCoBan))
                        i= i+1
                    print("Moi nhap STT cau thu muon mua: ")
                    n = int(input())
                    temp[n].dNgayGiaNhap = 2021
                    print("Ban muon ki hop dong thoi han bao lau: ")
                    thoihan = int(input())
                    temp[n].iThoiGianHopDong = thoihan
                    temp[n].sNghe = "CauThu"
                    qlct.lDsCauThu.append(temp[n])
                    temp.pop(n)
                    print("Successfully ~~ ")
                if(choice1 == 2):
                    i = 0
                    for item in qlct.lDsCauThu: 
                        print("STT: " + str(i) + " Ho ten: " + str(item.sHoTen) + " Luong: " + str(item.dLuongCoBan))  
                        i = i+1
                    print("Ban muon ban cau thu so may: ") 
                    stt = int(input())
                    qlct.xoa1CT(stt)
                    print("Successfully ~~ ")                  
                if(choice1 == 3):     
                    flag = 0

class Program:
    def Main(relf):
        flag = int(1)
        a = DoiBong()
        a.Nhap()
        san = San()
        co = 1
        co2 = 1
        co3 = 0
        co4 = 0
        while (flag == 1):
            print("\t\t\t************************MENU************************\t\t\t")
            print("\t\t\t***            1. Quan Ly Cau Thu                ***\t\t\t")
            print("\t\t\t***            2. Quan Ly Nhan Vien              ***\t\t\t")
            print("\t\t\t***            3. Quan Ly San                    ***\t\t\t")
            print("\t\t\t***            4. Hoat Dong                      ***\t\t\t")
            print("\t\t\t***            5. Thoat                          ***\t\t\t")
            print("\t\t\t****************************************************\t\t\t")
            print("Moi nhap lua chon cua ba => Your choice: ")
            choice = int(input())
            if( choice == 1):
                    a.MenuQLCT()
                    co3 = 1
            if( choice == 2):
                    a.MenuQLNV()
                    co4 = 1 
            if( choice == 3):
                    if (co == 1):
                        print("Doi Bong co san co khong? 1_Co || 2_Khong : ")
                        temp = int(input())
                        if (temp == 1):
                            san.Nhap()
                            print("//////////////////////////////////////////////////////////////////////")
                            san.Xuat()
                        else:
                            co2 = 0
                            san = None
                            print("Doi bong khong co San!! ")
                        co = 0
                    else:
                        if (co2 == 1):
                            san.Xuat()
                        else:
                            print("Doi bong khong co San!! ")
                    
            if( choice == 4):
                    if (co3 == 1 & co4 == 1):
                        a.MenuHoatDong()
                    else:
                        print("Yeu cau phai nhap 1 va 2 truoc moi co the su dung Tinh Nang nay !!")
            if( choice == 5):
                    flag = 0

    
                        
                
            
        
# instantiate the Car class
toyota = Program()
toyota.Main()
