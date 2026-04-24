VERSION 5.00
Begin VB.Form test 
   Caption         =   "тест оборудывания"
   ClientHeight    =   7170
   ClientLeft      =   60
   ClientTop       =   345
   ClientWidth     =   11085
   LinkTopic       =   "Form1"
   ScaleHeight     =   7170
   ScaleWidth      =   11085
   StartUpPosition =   3  'Windows Default
   Begin VB.CommandButton pusk 
      Caption         =   "ПУСК"
      Height          =   375
      Left            =   4320
      TabIndex        =   20
      Top             =   6480
      Width           =   1335
   End
   Begin VB.CommandButton konec 
      Caption         =   "Выход"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   12
         Charset         =   204
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   375
      Left            =   6840
      TabIndex        =   16
      Top             =   6480
      Width           =   1935
   End
   Begin VB.TextBox rez 
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   12
         Charset         =   204
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   3375
      Left            =   480
      MultiLine       =   -1  'True
      ScrollBars      =   2  'Vertical
      TabIndex        =   14
      Top             =   3720
      Width           =   2535
   End
   Begin VB.Frame Frame1 
      Caption         =   "Параметры"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   12
         Charset         =   204
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   5535
      Left            =   6120
      TabIndex        =   2
      Top             =   480
      Width           =   4575
      Begin VB.CommandButton Command1 
         Caption         =   "ВЫКЛЮЧ"
         Height          =   375
         Left            =   120
         TabIndex        =   22
         Top             =   1800
         Width           =   855
      End
      Begin VB.CommandButton coman 
         Caption         =   "ВКЛЮЧ"
         Height          =   375
         Left            =   3720
         TabIndex        =   21
         Top             =   1800
         Width           =   735
      End
      Begin VB.Timer Timer1 
         Left            =   2880
         Top             =   600
      End
      Begin VB.TextBox Text9 
         BeginProperty Font 
            Name            =   "MS Sans Serif"
            Size            =   12
            Charset         =   204
            Weight          =   400
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         Height          =   375
         Left            =   2400
         TabIndex        =   19
         Text            =   "2"
         Top             =   4680
         Width           =   1215
      End
      Begin VB.TextBox Text8 
         BeginProperty Font 
            Name            =   "MS Sans Serif"
            Size            =   12
            Charset         =   204
            Weight          =   400
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         Height          =   360
         Left            =   360
         TabIndex        =   18
         Text            =   "10"
         Top             =   5040
         Width           =   1215
      End
      Begin VB.TextBox koltochek 
         BeginProperty Font 
            Name            =   "MS Sans Serif"
            Size            =   12
            Charset         =   204
            Weight          =   400
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         Height          =   360
         Left            =   2040
         TabIndex        =   12
         Text            =   "1024"
         Top             =   3360
         Width           =   1335
      End
      Begin VB.TextBox koldat 
         BeginProperty Font 
            Name            =   "MS Sans Serif"
            Size            =   12
            Charset         =   204
            Weight          =   400
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         Height          =   360
         Left            =   360
         TabIndex        =   10
         Text            =   "8"
         Top             =   3360
         Width           =   1215
      End
      Begin VB.TextBox bps 
         BeginProperty Font 
            Name            =   "MS Sans Serif"
            Size            =   12
            Charset         =   204
            Weight          =   400
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         Height          =   405
         Left            =   2640
         TabIndex        =   8
         Text            =   "1"
         Top             =   1800
         Width           =   855
      End
      Begin VB.TextBox ampl 
         BeginProperty Font 
            Name            =   "MS Sans Serif"
            Size            =   12
            Charset         =   204
            Weight          =   400
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         Height          =   375
         Left            =   1200
         TabIndex        =   6
         Text            =   "0.333"
         Top             =   1800
         Width           =   975
      End
      Begin VB.TextBox chast 
         BeginProperty Font 
            Name            =   "MS Sans Serif"
            Size            =   12
            Charset         =   204
            Weight          =   400
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         Height          =   420
         Left            =   600
         TabIndex        =   3
         Text            =   "2.13456"
         Top             =   720
         Width           =   1455
      End
      Begin VB.Label Label9 
         Caption         =   "Частота              Кадр.задержка(Мсек)  квантов.(Кгц)"
         BeginProperty Font 
            Name            =   "MS Sans Serif"
            Size            =   12
            Charset         =   204
            Weight          =   400
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         Height          =   615
         Left            =   120
         TabIndex        =   17
         Top             =   4320
         Width           =   4335
      End
      Begin VB.Label Label6 
         Caption         =   "Кол-во точек"
         BeginProperty Font 
            Name            =   "MS Sans Serif"
            Size            =   12
            Charset         =   204
            Weight          =   400
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         Height          =   615
         Left            =   2280
         TabIndex        =   11
         Top             =   2640
         Width           =   975
      End
      Begin VB.Label Label5 
         Caption         =   "Количество датчиков"
         BeginProperty Font 
            Name            =   "MS Sans Serif"
            Size            =   12
            Charset         =   204
            Weight          =   400
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         Height          =   735
         Left            =   360
         TabIndex        =   9
         Top             =   2640
         Width           =   1335
      End
      Begin VB.Label Label4 
         Caption         =   "Номер(БПС) генератора"
         BeginProperty Font 
            Name            =   "MS Sans Serif"
            Size            =   12
            Charset         =   204
            Weight          =   400
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         Height          =   615
         Left            =   2520
         TabIndex        =   7
         Top             =   1200
         Width           =   1455
      End
      Begin VB.Label Label3 
         Caption         =   "Амплитуда"
         BeginProperty Font 
            Name            =   "MS Sans Serif"
            Size            =   12
            Charset         =   204
            Weight          =   400
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         Height          =   375
         Left            =   1080
         TabIndex        =   5
         Top             =   1440
         Width           =   1335
      End
      Begin VB.Label Label2 
         Caption         =   "Частота"
         BeginProperty Font 
            Name            =   "MS Sans Serif"
            Size            =   12
            Charset         =   204
            Weight          =   400
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         Height          =   375
         Left            =   480
         TabIndex        =   4
         Top             =   360
         Width           =   1455
      End
   End
   Begin VB.TextBox Text1 
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   12
         Charset         =   204
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   375
      Left            =   4200
      TabIndex        =   1
      Text            =   "8"
      Top             =   5400
      Width           =   1095
   End
   Begin VB.Label Label8 
      Caption         =   "Результат"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   12
         Charset         =   204
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   255
      Left            =   600
      TabIndex        =   15
      Top             =   3360
      Width           =   2175
   End
   Begin VB.Label Label7 
      Caption         =   $"Formzad_kom.frx":0000
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   12
         Charset         =   204
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   3135
      Left            =   240
      TabIndex        =   13
      Top             =   240
      Width           =   5775
   End
   Begin VB.Label Label1 
      Caption         =   "Кoманда(1-13)"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   12
         Charset         =   204
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   375
      Left            =   3960
      TabIndex        =   0
      Top             =   4920
      Width           =   1815
   End
End
Attribute VB_Name = "test"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
 
Dim kolData&, pp$, koltim%
   Private Declare Sub CopyMemory Lib "kernel32" Alias "RtlMoveMemory" _
         (hpvDest As Any, hpvSource As Any, ByVal cbCopy As Long)
   Private Declare Function IsClipboardFormatAvailable Lib "user32" (ByVal wFormat As Long) As Long
   Private Declare Function OpenClipboard Lib "user32" (ByVal hwnd As Long) As Long
   Private Declare Function CloseClipboard Lib "user32" () As Long
   Private Declare Function GetClipboardData Lib "user32" (ByVal wFormat As Long) As Long
   Private Declare Function GlobalLock Lib "kernel32" (ByVal hMem As Long) As Long
   Private Declare Function GlobalSize Lib "kernel32" (ByVal hMem As Long) As Long
   Private Declare Function GlobalUnlock Lib "kernel32" (ByVal hMem As Long) As Long
   Private Declare Sub Sleep Lib "kernel32" (ByVal dwMilliseconds As Long)



Private Sub Command1_Click()
'ВЫКЛЮЧЕНИЕ СИЛЫ

End Sub

Private Sub pusk_Click() 'передача
 Dim pp$
 If (Text1.Text = "1") Then pp = Str("1") & "," & chast.Text & ",\" & Str(20) & ":"
 If (Text1.Text = "2") Then pp = Str("2") & "," & ampl.Text & "," & bps.Text & ",\" & Str(21) & ":"
 If (Text1.Text = "3") Then pp = Str("3") & ",\" & bps.Text & "," & Str(0) & ":"
 If (Text1.Text = "4") Then pp = Str("4") & "," & chast.Text & "," & ampl.Text & ",\" & Str(1) & ":"
 If (Text1.Text = "5") Then pp = Str("5") & "," & chast.Text & ",\" & Str(24) & ":"
 If (Text1.Text = "6") Then pp = Str("6") & "," & chast.Text & ",\" & Str(25) & ":"
 If (Text1.Text = "7") Then pp = Str("7") & "," & chast.Text & ",\" & Str(26) & ":"
 If (Text1.Text = "8") Then pp = Str("8") & "," & koltochek.Text & "," & koldat.Text & ",\" & Str(27) & ":"
 If (Text1.Text = "13") Then pp = Str("13") & "," & Str("44") & ",\" & Str(28) & ":"""
 
 Clipboard.SetText pp
'time peredachi = 2.8mcek
'ожидание приема результата
rez.Text = " "

Call buffer

End Sub

Private Sub buffer()
Dim pp1$, kom1%, nac%, kd1%, kon%, chis!(300), re!(100), im!(100), ff$
Dim kd%, i%, ii%, imemsize&

mm3:
DoEvents

pp1 = PasteBuffer(imemsize)
i = InStr(1, pp1, "\") + 1
ff = Mid(pp1, i, 3)
ii = Val(ff)                '-27
 If ii >= 0 Then GoTo mm3
'РАСШИФРОВКА РЕЗУЛЬТАТА
'

'pp1 = "-1.25,10.25,2.25,-11.25,3.25,12.25,4.23,-13.23,5.22,14.22,6.22,15.22,7.23,16.22,8.22,17.22,\"
kd1 = InStr(1, pp1, "\")

 nac = 1
 For i = 1 To kd1
  kom1 = InStr(nac, pp1, ",")
  If kom1 = 0 Then GoTo mm1
  ff = Mid(pp1, nac, (kom1 - nac))
  chis(i) = Val(ff)
  kom1 = kom1 + 1
  nac = kom1
 Next i
mm1:
 kd = (i - 1) / 2
 'Debug.Print kd
   ii = 0
   For i = 1 To kd
  
  re(i) = chis(ii + 1)
  im(i) = chis(ii + 2)
  
  ii = ii + 2
   Next i
    For i = 1 To kd
   rez.Text = rez.Text & Str(i) & "   " & Str(re(i)) & "    " & Str(im(i)) & vbCrLf
   
   Next i
'mm2:
End Sub


'выход
Private Sub konec_Click() 'выход
pp = "13,444,\"
Clipboard.SetText pp
End
End Sub



Private Sub Form_Load()
'Clipboard.Clear
'Shell "priem.exe", 1
'ожидание приема результата

End Sub
   




Private Function PasteBuffer(imemsize) As String
Dim hMem&, pMem&, sText$
CF_TEXT = 1
PasteBuffer = ""
If IsClipboardFormatAvailable(CF_TEXT) = 0 Then
Exit Function
End If
 If OpenClipboard(Me.hwnd) <> 0 Then
   hMem = GetClipboardData(CF_TEXT)
    If hMem = 0 Then
     CloseClipboard
     Exit Function
    Else
    pMem = GlobalLock(hMem)
    imemsize = GlobalSize(hMem)
    sText = String$(imemsize, 0)
     CopyMemory ByVal sText, ByVal pMem, imemsize
    GlobalUnlock hMem
    CloseClipboard
    PasteBuffer = Trim(sText)
    End If
  End If
 ' Debug.Print pMem, hMem, sText
  
End Function

