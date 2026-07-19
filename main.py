import math
from datetime import datetime
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

class MyCalculationApp(App):
    def build(self):
        # ترتيب الواجهة بشكل عمودي
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # خانات الإدخال 
        self.txt_y = TextInput(hint_text="ادخل عدد الحمايات (مثال: 2)", multiline=False, size_hint_y=None, height=45)  
        self.txt_t = TextInput(hint_text="ادخل الأطوال مفصولة بمسافة (مثال: 120 150)", multiline=False, size_hint_y=None, height=45)  
        self.txt_w = TextInput(hint_text="ادخل الأعراض مفصولة بمسافة (مثال: 80 95)", multiline=False, size_hint_y=None, height=45)  
        self.txt_g = TextInput(hint_text="ادخل الجالس بترتيب مفصولة بمسافة (مثال: 15 20)", multiline=False, size_hint_y=None, height=45)  
        self.txt_p = TextInput(hint_text="ادخل سعر المتر المربع", multiline=False, size_hint_y=None, height=45)  
        self.txt_ys = TextInput(hint_text="ادخل سعر الصرف اليوم", multiline=False, size_hint_y=None, height=45)  
          
        layout.add_widget(self.txt_y)  
        layout.add_widget(self.txt_t)  
        layout.add_widget(self.txt_w)  
        layout.add_widget(self.txt_g)  
        layout.add_widget(self.txt_p)  
        layout.add_widget(self.txt_ys)  
          
        # زر التشغيل والحساب  
        btn = Button(text="احسب واطبع النتائج", size_hint_y=None, height=50, background_color=(0.1, 0.6, 0.2, 1))  
        btn.bind(on_press=self.run_your_code)  
        layout.add_widget(btn)  
          
        # شاشة صغيرة لعرض النتائج  
        scroll = ScrollView()  
        self.lbl_res = Label(text="النتائج ستظهر هنا...", size_hint_y=None, font_size='16sp', halign='center')  
        self.lbl_res.bind(texture_size=self.lbl_res.setter('size'))  
        scroll.add_widget(self.lbl_res)  
        layout.add_widget(scroll)  
          
        return layout  

    def run_your_code(self, instance):  
        try:  
            y = int(self.txt_y.text)  
            input_t = [int(n) for n in self.txt_t.text.split()]  
            input_w = [int(n) for n in self.txt_w.text.split()]  
            input_g = [int(n) for n in self.txt_g.text.split()]  
            p = float(self.txt_p.text)  # تم التعديل إلى float لدعم الكسور
            ys = float(self.txt_ys.text) # تم التعديل إلى float لدعم الكسور
            
            x = 0 ; ww=0 ; tt =0 ; gg =0 ; aa=0  
            lt = [] ; lw = [] ; lx = [] ; lg = [] ; lh = [] ; la = []  
              
            num = list(range(1, y+1))  
            for i in num:  
                t = input_t[i-1]  
                w = input_w[i-1]  
                x += t * w / 10000  
                lt.append(t)  
                lw.append(w)  
                lx.append(x)  
                tt += t  
                ww += w  
                  
            output = f" اجمالي المساحة  =  {x}  متر مربع \n\n"  
            output += "اجمالي السعر  = \n"  
            output += f"{x * p}   ريال يمني  \n"  
            output += f"{(x * p) / ys:.2f}   ريال سعودي  \n\n"  
            
            for i in num:  
                g = input_g[i-1]  
                lg.append(g)  
                gg += g  
                
            for i in num:  
                h = lt[i-1] - lg[i-1]  
                if h <= 0: h = 0.001  
                lh.append(h)  
                r = (h / 2) + (lw[i-1]**2 / (8 * h))  
                z = lw[i-1] / (2 * r)  
                z = max(-1.0, min(1.0, z))  
                s = math.asin(z)  
                arc = 2 * s * r  
                la.append(arc)  
                aa += arc  
                  
            for i in num:  
                output += f"طول العقد  {i}  : {la[i-1]:.2f}\n"  
                
            output += "\nيحتاج حديد \n\n"  
            output += f"{x * 3}   مربوع صم\n"  
            output += f"{((2 * gg) + ww + aa) / 600:.4f}   شلمان \n"  
              
            self.lbl_res.text = output  
              
            with open("history_log.txt", "a", encoding="utf-8") as f:  
                f.write(f"--- حُفظ بتاريخ {datetime.now().strftime('%Y-%m-%d %H:%M')} ---\n")  
                f.write(output)  
                f.write("\n" + "="*40 + "\n")  
                  
        except Exception as e:  
            self.lbl_res.text = f"خطأ: تأكد من إدخال الأرقام في كل الخانات بشكل صحيح!\n({str(e)})"

if __name__ == '__main__':
    MyCalculationApp().run()
            
