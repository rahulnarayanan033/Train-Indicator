from tkinter import *
class node(): 
    def __init__(self,val): 
        self.val = val 
        self.left = None
        self.right = None
        self.height = 1
class Avl():
    #insert the node
    def insert(self,root,data): 
        if not root: 
            return node(data) 
        elif data < root.val: 
            root.left = self.insert(root.left, data) 
        else: 
            root.right = self.insert(root.right, data) 

        #Calculate the height
        root.height = 1 + max(self.height(root.left), 
                           self.height(root.right))

        #Calculate balance of tree
        bal = self.balance(root) 
  
        if bal>1 and data<root.left.val: 
            return self.rrotate(root) 
  
        if bal<-1 and data>root.right.val: 
            return self.lrotate(root) 
  
        if bal>1 and data>root.left.val: 
            root.left = self.lrotate(root.left) 
            return self.rrotate(root) 
  
        if bal<-1 and data<root.right.val: 
            root.right = self.rrotate(root.right) 
            return self.lrotate(root) 
  
        return root 
  
    def lrotate(self,root): 
      
        nroot = root.right 
        rt = nroot.left 
  
        #for rotation 
        nroot.left = root 
        root.right = rt 
  
        #Update heights 
        root.height = 1 + max(self.height(root.left), 
                         self.height(root.right))
        
        return nroot 
  
    def rrotate(self,root): 
  
        nroot = root.left 
        lt = nroot.right 
  
        nroot.right = root 
        root.left = lt
  
        root.height = 1 + max(self.height(root.left), 
                        self.height(root.right)) 
        
        return nroot
    
  
    def height(self,root): 
        if not root: 
            return 0
        
        return root.height 
  
    def balance(self,root): 
        if not root: 
            return 0
        return self.height(root.left) - self.height(root.right) 
  
    def print(self,root):
        if not root: 
            return
        self.print(root.left)
        h=Label(g,text=root.val)
        h.pack()
        self.print(root.right)
    
t = Avl()
t1=Avl()
t2=Avl()
#t4=Avl()
t5=Avl()
t6=Avl()
t7=Avl()
t8=Avl()
t9=Avl()
t10=Avl()
t11=Avl()
t12=Avl()
root = None
gui=Tk()
g=Tk()
def Central():
    w=Label(gui,text="Where are you?")
    w.pack()
    
    def Kalyan():
        root=0
        root = t.insert(root, '\n10:06\tCSMT\tPf:1') 
        root = t.insert(root, '\n10:17\tAmbernath\tPf:2') 
        root = t.insert(root, '\n10:27\tDadar\tPf:6') 
        root = t.insert(root, '\n10:45\tCSMT\tPf:1') 
        root = t.insert(root, '\n11:00\tKarjat\tPf:4') 
        root = t.insert(root, '\n11:15\tCSMT\tPf:1A')
        root=t.insert(root,'\n11:30\tTitwala\tPf:2')
        l=Label(g,text='Kalyan')
        l.pack()
        t.print(root)
    k=Button(gui,text='Kalyan',command=Kalyan)
    k.pack()
    
    def Thane():
        root=0
        root = t1.insert(root, '\n10:20\tCsmt\tPf:1') 
        root = t1.insert(root, '\n10:40\tDombivili\rPf:3') 
        root = t1.insert(root, '\n10:50\tDadar\tPf:4') 
        root = t1.insert(root, '\n11:00\tKasara\tPf:5') 
        root = t1.insert(root, '\n11:20\tKalyan\tPf:2') 
        root = t1.insert(root, '\n11:40\tKurla\tPf:1')
        root= t1.insert(root,'\n11:50\tCsmt\tPf:3')
        l=Label(g,text='Thane')
        l.pack()
        t1.print(root)
    T1=Button(gui,text='Thane',command=Thane)
    T1.pack()

    def Ghatkopar():
        root=0
        root = t5.insert(root, '\n10:24\tDadar\tPf:1') 
        root = t5.insert(root, '\n10:27\tCsmt\tPf:4') 
        root = t5.insert(root, '\n10:34\tKalyan\tPf:1') 
        root = t5.insert(root, '\n11:39\tDombivli\tPf:3') 
        root = t5.insert(root, '\n11:02\tCSMT\tPf:2') 
        root = t5.insert(root, '\n11:15\tKurla\tPf:3')
        root= t5.insert(root,'\n11:34\tKalyan\tPf:4')
        l=Label(g,text='Ghatkopar')
        l.pack()
        t5.print(root)
    G1=Button(gui,text='Ghatkopar',command=Ghatkopar)
    G1.pack()

    def csmt():
        root=0
        root = t2.insert(root, '\n10:36\tDadar\tPf:3') 
        root = t2.insert(root, '\n10:45\tBadlapur\tPf:5') 
        root = t2.insert(root, '\n10:50\tKalyan\tPf:7') 
        root = t2.insert(root, '\n10:55\tDombivli\tPf:4') 
        root = t2.insert(root, '\n11:02\tThane\tPf:5') 
        root = t2.insert(root, '\n11:15\tKurla\tPf:6')
        root= t2.insert(root,'\n11:35\tKalyan\tPf:1')
        l=Label(g,text='Csmt')
        l.pack()
        t2.print(root)
    cs=Button(gui,text='CSMT',command=csmt)
    cs.pack()

def western():
    wes=Label(gui,text='Where are you?')
    wes.pack()
    def ch():
        root=0
        root = t10.insert(root, '\n12:16\tGhatkopar\t') 
        root = t10.insert(root, '\n12:34\tVersova\t') 
        root = t10.insert(root, '\n12:59\tVersova') 
        root = t10.insert(root, '\n1:16\tGhatkopar') 
        root = t10.insert(root, '\n2:07\tVersova') 
        root = t10.insert(root, '\n2:36\tGhatkopar')
        root= t10.insert(root,'\n2:45\tGhatkopar')
        l=Label(g,text='Churchgate')
        l.pack()
        t10.print(root)
    chu=Button(gui,text='Churchgate',command=ch)
    chu.pack()
    def an():
        root=0
        root = t11.insert(root, '\n8:30\tBhayandar\tPf:3') 
        root = t11.insert(root, '\n8:35\tVasai\tPf:1') 
        root = t11.insert(root, '\n8:40\tVirar\tPf:2') 
        root = t11.insert(root, '\n8:45\tVirar\tPf:4') 
        root = t11.insert(root, '\n8:50\tBorivali\tPf:1') 
        root = t11.insert(root, '\n8:55\tDahanu\tPf:3')
        root= t11.insert(root,'\n9:00\tVasai\tPf:2')
        l=Label(g,text='Andheri')
        l.pack()
        t11.print(root)
    andh=Button(gui,text='Andheri',command=an)
    andh.pack()
    def dr():
        root=0
        root = t12.insert(root, '\n8:30\tChurchgate\tPf:1') 
        root = t12.insert(root, '\n8:35\tChurchgate\tPf:2') 
        root = t12.insert(root, '\n8:40\tChurchgate\tPf:1') 
        root = t12.insert(root, '\n8:45\tVirar\tPf:3') 
        root = t12.insert(root, '\n8:50\tBhayander\tPf:4') 
        root = t12.insert(root, '\n8:55\tGoregaon\tPf:3')
        root= t12.insert(root,'\n9:00\tVasai\tPf:4')
        l=Label(g,text='Dadar')
        l.pack()
        t12.print(root)
    dad=Button(gui,text='Dadar',command=dr)
    dad.pack()

def Metro():
    v=Label(gui,text='Where are you')
    v.pack()
    def sk():
        root=0
        root = t7.insert(root, '\n8:30\tGhatkopar') 
        root = t7.insert(root, '\n8:35\tVersova') 
        root = t7.insert(root, '\n8:40\tVersova') 
        root = t7.insert(root, '\n8:45\tGhatkopar') 
        root = t7.insert(root, '\n8:50\tVersova') 
        root = t7.insert(root, '\n8:55\tGhatkopar')
        root= t7.insert(root,'\n9:00\tGhatkopar')
        l=Label(g,text='Sakinaka')
        l.pack()
        t7.print(root)
    s=Button(gui,text='Saki Naka',command=sk)
    s.pack()
    def dn():
        root=0
        root = t8.insert(root, '\n8:00\tVersova') 
        root = t8.insert(root, '\n8:20\tGhatkopar') 
        root = t8.insert(root, '\n8:30\tVersova') 
        root = t8.insert(root, '\n8:35\tGhatkopar') 
        root = t8.insert(root, '\n8:40\tVersova') 
        root = t8.insert(root, '\n8:45\tGhatkopar')
        root= t8.insert(root,'\n8:55\tVersova')
        l=Label(g,text='DN Nagar')
        l.pack()
        t8.print(root)
    d=Button(gui,text='DN Nagar',command=dn)
    d.pack()
    def asa():
        root=0
        root = t9.insert(root, '\n8:30\tGhatkopar') 
        root = t9.insert(root, '\n8:35\tVersova') 
        root = t9.insert(root, '\n8:40\tGhatkopar') 
        root = t9.insert(root, '\n8:45\tVersova') 
        root = t9.insert(root, '\n8:50\tGhatkopar') 
        root = t9.insert(root, '\n9:00\tVersova')
        root= t9.insert(root,'\n9:15\tGhatkopar')
        l=Label(g,text='Asalpha')
        l.pack()
        t9.print(root)
    a=Button(gui,text='Asalpha',command=asa)
    a.pack()
def harbour():
    w=Label(gui,text="where you are?")
    w.pack()
    
        
    def cs():
        root=0
        root = t9.insert(root, '\n10:10\tPanvel\t\tPlatForm:2') 
        root = t9.insert(root, '\n10:25\tVashi\t\tPlatForm:2') 
        root = t9.insert(root, '\n10:44\tKurla\t\tPlatForm:2')
        root = t9.insert(root, '\n11:00\tPanvel\t\tPlatForm:2')
        root = t9.insert(root, '\n11:17\tPanvel\t\tPlatForm:2')
        l=Label(g,text='Csmt')
        l.pack()
        t9.print(root)
    

    def wd():
        root=0
        root = t10.insert(root, '\n1:48\tNerul\t\tPlatform:4') 
        root = t10.insert(root, '\n1:57\tNerul\t\tPlatForm:4')
        root = t10.insert(root, '\n2:14\tPanvel\t\tPlatForm:4')
        root = t10.insert(root, '\n2:21\tCSMT\t\tPlatForm:4')
        root = t10.insert(root, '\n2:37\tPanvel\t\tPlatForm:4')
        l=Label(g,text='Wadala')
        l.pack()
        t10.print(root)

    def vs():
        root=0
        #t.print(root)
        root = t11.insert(root, '\n3:00\tCSMT\t\tPlatform:3') 
        root = t11.insert(root, '\n3:13\tCSMT\t\tPlatForm:3')
        root = t11.insert(root, '\n3:26\tPanvel\t\tPlatForm:3')
        root = t11.insert(root, '\n3:39\tCSMT\t\tPlatForm:3')
        root = t11.insert(root, '\n3:52\tPanvel\t\tPlatForm:3')
        l=Label(g,text='Vasai')
        l.pack()
        t11.print(root)

    def pn():
        root=0
        #t.print(root)
        root = t12.insert(root, '\n7:43\tCSMT\t\tPlatform:2') 
        root = t12.insert(root, '\n7:51\tCSMT\t\tPlatForm:2')
        root = t12.insert(root, '\n8:09\tCSMT\t\tPlatForm:2')
        root = t12.insert(root, '\n8:13\tKurla\t\tPlatForm:2')
        root = t12.insert(root, '\n8:21\tCSMT\t\tPlatForm:2')
        l=Label(g,text='Panvel')
        l.pack()
        t12.print(root)
    h1=Button(gui,text='CSMT',command=cs)
    h1.pack()
    h1=Button(gui,text='Wadala',command=wd)
    h1.pack()
    h1=Button(gui,text='Vasai',command=vs)
    h1.pack()
    h1=Button(gui,text='Panvel',command=pn)
    h1.pack()

cen=Button(gui,text='Central',command=Central)
cen.pack()
we=Button(gui,text='Western',command=western)
we.pack()
har=Button(gui,text='Harbour',command=harbour)
har.pack()
m=Button(gui,text='Metro',command=Metro)
m.pack()
def quits():
    gui.destroy()
    g.destroy()
q=Button(gui,text='Quit',command=quits)
q.pack()
gui.mainloop()


