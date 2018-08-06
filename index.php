<html>
<title>
</title>

<body>


<?php

$message = exec("/var/www/scripts/test.py 2>&1");
print_r($message);

?>
</body>
</html>