<? include "header.php"; ?>

<div>
<form action="php/upload_file.php" method="POST"
enctype="multipart/form-data">
<label for="file">Filename:</label>
<input type="file" name="file" id="file"><br>
<input type="submit" name="submit" value="Submit">
</form>
</div>

<? include "footer.php"; ?>