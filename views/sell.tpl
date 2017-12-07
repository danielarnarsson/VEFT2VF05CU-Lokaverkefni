<html>
<head>
	<link type="text/css" href="/static/css/styles.css" rel="stylesheet">
</head>
<body>
<div>
<h1>Skráning</h1>
<a></a>
</div>
<form method="post" action="/sell" enctype="multipart/form-data">
	<select name="category">
		<option value="Books">Books</option>
		<option value="Cars">Cars</option>
		<option value="Computers">Computers</option>
	</select>
	<br>
	<br>
	<b>Titill</b>
	<br>
	<input type="text" name="title" maxlength=100 required/>
	<br>
	<br>
	<b>Verð</b>
	<br>
	<input type="number" name='price' maxlength=16 required/><b> kr</b>
	<br>
	<br>
	<b>Upplýsingar</b>
	<br>
	<textarea name="info" rows=10 cols=50 maxlength=1000 required></textarea>
	<br>
	<br>
<input type="submit"/>
</form>
%try:
	%if saved == True:
		<h2>Vara vistuð.</h2>
		<a href="/">Til baka</a>
		%pass
		%end
	%end
%except:
	<p>Method not allowed.</p>
%end
</body>
</html>