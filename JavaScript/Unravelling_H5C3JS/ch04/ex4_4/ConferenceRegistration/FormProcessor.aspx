<%@ Page Language="C#" %>

<!DOCTYPE html>

<html>
<head runat="server">
    <title>Form Processor</title>
    <style>
      body {
        font-family: Verdana, Arial, sans-serif;
        margin-left: 24px;
      }
      table {
        border: 2px solid dimgray;
        border-collapse: collapse;
      }

      td, th {
        padding: 4px 8px;
        border: 1px dotted dimgray;
      }

      th {
        background-color: dimgray;
        color: white;
      }
    </style>
</head>
<body>
  <h2>Form Data</h2>
  <table>
    <tr>
      <th>Property</th>
      <th>Value</th>
    </tr>
    <%
      var parameters = Request.QueryString;
    %>
    <% foreach (var prop in parameters.AllKeys)
       {
    %>
    <tr>
      <td><% =prop %></td>
      <td><% =parameters[prop] %></td>
    </tr>
    <%
       }
    %>
  </table>
</body>
</html>
