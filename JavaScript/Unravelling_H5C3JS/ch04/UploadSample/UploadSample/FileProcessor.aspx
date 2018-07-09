<%@ Page Language="C#" 
  AutoEventWireup="true" 
  CodeBehind="FileProcessor.aspx.cs" 
  Inherits="UploadSample.FileProcessor" %>

<!DOCTYPE html>
<html>
<head runat="server">
  <title>File Upload</title>
  <link href="style.css" rel="stylesheet" />
</head>
<body>
    <h1>Upload a File</h1>
    <form id="form1" runat="server" enctype="multipart/form-data">
    <label>
      Select a file:
      <input id="uploadedFile" name="file" type="file" />
    </label>
    <br />
    <input type="submit" value="Upload" />
    </form>
</body>
</html>
