VERSION 5.00
Begin VB.Form прием 
   Caption         =   "ПРИЕМ"
   ClientHeight    =   1290
   ClientLeft      =   60
   ClientTop       =   9870
   ClientWidth     =   11385
   FillColor       =   &H0080FF80&
   ForeColor       =   &H8000000C&
   LinkTopic       =   "Form1"
   ScaleHeight     =   1290
   ScaleWidth      =   11385
   Begin VB.TextBox Text2 
      Height          =   405
      Left            =   240
      TabIndex        =   1
      Text            =   "Text2"
      Top             =   120
      Width           =   10335
   End
   Begin VB.TextBox Text1 
      Height          =   375
      Left            =   1800
      TabIndex        =   0
      Text            =   "чтение буфера"
      Top             =   840
      Width           =   1575
   End
   Begin VB.Timer Timer1 
      Left            =   600
      Top             =   720
   End
End
Attribute VB_Name = "прием"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Dim idat%(32767), Nkom!(400), re!(32), im!(32), kd%
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

Private Sub vubor()
Dim ii%, i%, pp$
'--------------------------------
                    kd = 8
'text2 там - номер sub,param,\
'----------------------------
ii = Nkom(1)
On Error GoTo loop1
Clipboard.Clear

loop1:
Select Case ii
Case 1

ret = zfreq(Nkom(2))
Case 2
Case 3
ret = zcil(ii, Nkom(2), 0)
Case 4
ret = zcil(ii, Nkom(2), 1)
Case 5
Case 6
Case 7
Case 7
Case 8

ret = izm
Timer1.Enabled = True

Case 9
Case 10
Case 11
Case 12
Case 13


End
End Select

End Sub

Private Sub za()
Dim pp1$, vp1&, ff$, nac&, kon&, imemsize&, chis!, kom1%


pp1 = PasteBuffer(imemsize) 'принял буфер

'pp1 = "8,2.3456,\"
                vp1 = InStr(1, pp1, "\")

kom1 = 0
 nac = 1
 For i = 1 To vp1
  kon = InStr(nac, pp1, ",")
  If kon = 0 Then GoTo mm1
  ff = Mid(pp1, nac, kon - nac)
  chis = Val(ff)
  kom1 = kom1 + 1
  Nkom(kom1) = chis
  nac = kon + 1
 Next i
mm1:
                        If pp1 <> "" Then Text1.Text = pp1
     Call vubor
End Sub

Private Function PasteBuffer(imemsize) As String 'принял буфер
Dim hMem&, pMem&, sText$
CF_TEXT = 1
PasteBuffer = ""
If IsClipboardFormatAvailable(CF_TEXT) = 0 Then
Exit Function
End If
'Debug.Print "        " & Me.hwnd


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
End Function

Private Function zfreq(freq1)
'установка частоты
Sleep (120)
End Function
Private Function zcil(ampl, nom1, bkl)
'установка силы
If bkl = 0 Then
  nom = 1
  Else
  nom = 0
 zcil = 1
 End If
End Function

Private Function izm() As Integer

Dim pp$
 izm = 0

     For i = 1 To kd
      re(i) = i + 0.25
      im(i) = i + 10.25
     Next i
     For i = 1 To kd
      pp = pp & Str(re(i)) & "," & Str(im(i)) & ","
     Next i
      pp = pp & "\" & Str(-27) & ":"
Text2.Text = pp

Sleep (2600)
On Error GoTo loop2
Clipboard.SetText pp
izm = 1
loop2:
End Function



Private Sub Form_Load()
On Error GoTo loop3
Clipboard.Clear
loop3:
Timer1.Enabled = True
Timer1.Interval = 170
'top okna=8190,left=-60
'убрать форму с экрана
'прием.Hide

End Sub





Private Sub Timer1_Timer()
Call za

End Sub

