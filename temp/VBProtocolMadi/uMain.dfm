object MainForm: TMainForm
  Left = 0
  Top = 0
  Caption = 'VB Protocol Dummy (Madi)'
  ClientHeight = 400
  ClientWidth = 600
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'Tahoma'
  Font.Style = []
  OldCreateOrder = False
  OnCreate = FormCreate
  PixelsPerInch = 96
  TextHeight = 13
  object LabelIn: TLabel
    Left = 8
    Top = 8
    Width = 84
    Height = 13
    Caption = 'InEdit (Принято):'
  end
  object LabelOut: TLabel
    Left = 8
    Top = 200
    Width = 100
    Height = 13
    Caption = 'OutEdit (Отправка):'
  end
  object InEdit: TMemo
    Left = 8
    Top = 27
    Width = 584
    Height = 160
    ScrollBars = ssVertical
    TabOrder = 0
  end
  object OutEdit: TMemo
    Left = 8
    Top = 219
    Width = 584
    Height = 160
    ScrollBars = ssVertical
    TabOrder = 1
  end
  object Timer1: TTimer
    Enabled = False
    Interval = 170
    OnTimer = Timer1Timer
    Left = 544
    Top = 32
  end
end
