unit uMain;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, ExtCtrls, StdCtrls, Clipbrd;

type
  TMainForm = class(TForm)
    InEdit: TMemo;
    OutEdit: TMemo;
    Timer1: TTimer;
    LabelIn: TLabel;
    LabelOut: TLabel;
    procedure Timer1Timer(Sender: TObject);
    procedure FormCreate(Sender: TObject);
  private
    { Private declarations }
    fLastIn: string;
    procedure ProcessCommand(const lCmd: string);
    procedure SendResponse(const lResp: string);
  public
    { Public declarations }
  end;

var
  MainForm: TMainForm;

implementation

{$R *.dfm}

{ TMainForm }

procedure TMainForm.FormCreate(Sender: TObject);
begin
  fLastIn := '';
  Timer1.Interval := 170;
  Timer1.Enabled := True;
  
  InEdit.Clear;
  OutEdit.Clear;
end;

procedure TMainForm.Timer1Timer(Sender: TObject);
var
  lStr: string;
begin
  // Проверяем наличие текстового формата в буфере обмена
  if Clipboard.HasFormat(CF_TEXT) then
  begin
    try
      lStr := Clipboard.AsText;
      
      // Игнорируем пустые строки и то, что уже обработали (включая свой ответ)
      if (lStr <> '') and (lStr <> fLastIn) then
      begin
        // Согласно протоколу, команда заканчивается символом '\'
        if Pos('\', lStr) > 0 then
        begin
          fLastIn := lStr;
          InEdit.Lines.Add('>>> ' + lStr);
          ProcessCommand(lStr);
        end;
      end;
    except
      // Буфер может быть занят другим приложением
    end;
  end;
end;

procedure TMainForm.ProcessCommand(const lCmd: string);
var
  lID: string;
  lCommaPos: Integer;
  lResponse: string;
begin
  // Простейший парсер ID команды (до первой запятой)
  lCommaPos := Pos(',', lCmd);
  if lCommaPos > 0 then
    lID := Trim(Copy(lCmd, 1, lCommaPos - 1))
  else
    lID := Trim(StringReplace(lCmd, '\', '', [rfReplaceAll]));

  // Эмуляция логики
  if lID = '1' then // Частота
    SendResponse('ACK,1,\20:')
  else if lID = '8' then // Измерение
  begin
    // Возвращаем тестовые данные Re,Im и статус -27:
    lResponse := '1.1,10.1,2.2,20.2,3.3,30.3,4.4,40.4,\-27:';
    SendResponse(lResponse);
  end
  else if lID = '13' then // Выход
    SendResponse('BYE,13,\-28:')
  else if lID <> '' then
    SendResponse('ACK,' + lID + ',\-1:');
end;

procedure TMainForm.SendResponse(const lResp: string);
begin
  OutEdit.Lines.Add('<<< ' + lResp);
  try
    Clipboard.AsText := lResp;
    // Обновляем fLastIn, чтобы не срабатывать на собственный ответ
    fLastIn := lResp;
  except
    on E: Exception do
      OutEdit.Lines.Add('Error Clipboard: ' + E.Message);
  end;
end;

end.
