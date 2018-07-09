using System;
using System.IO;
using System.Web.UI;

namespace UploadSample
{
  public partial class FileProcessor : Page
  {
    protected void Page_Load(object sender, EventArgs e)
    {
      if (IsPostBack)
      {
        var file = Request.Files[0];
        var text = new StreamReader(file.InputStream)
          .ReadToEnd();
        Response.Write("<pre>" + text + "</pre>");
      }
    }
  }
}