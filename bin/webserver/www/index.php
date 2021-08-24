<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>SERVER STACK</title>
        <link rel="stylesheet" href="/assets/css/bulma.min.css">
    </head>
    <body>
        <section class="hero is-medium is-info is-bold">
            <div class="hero-body">
                <div class="container has-text-centered">
                    <h1 class="title">
                        SERVER STACK
                    </h1>
                    <h2 class="subtitle">
                        Your private development environment
                    </h2>
                </div>
            </div>
        </section>
        <section class="section">
            <div class="container">
                <div class="columns">
                    <div class="column">
                        <h3 class="title is-3 has-text-centered">Environment</h3>
                        <hr>
                        <div class="content">
                            <ul>
                                <li>PHP <?= phpversion(); ?></li>
                                <li>
                                    <?php
                                    $link = mysqli_connect("mysql", "root", "mysqladm", null);

/* check connection */
                                    if (mysqli_connect_errno()) {
                                        printf("MySQL connecttion failed: %s", mysqli_connect_error());
                                    } else {
                                        /* print server version */
                                        printf("MySQL Server %s", mysqli_get_server_info($link));
                                    }
                                    /* close connection */
                                    mysqli_close($link);
                                    ?>
                                </li>
                                <li>Owncloud</li>
                                <li>Jenkins</li>
                                <li>Linux Desktop noVNC</li>
                                <li>Redis</li>
                                <li>Portainer</li>

                            </ul>
                        </div>
                    </div>
                                        <?php
$host = "http://$_SERVER[HTTP_HOST]$_SERVER[REQUEST_URI]";
$host = substr_replace($host ,"", -1);

$endpoint = $_SERVER['SERVER_NAME']

?>

                    <div class="column">
                        <h3 class="title is-3 has-text-centered">Quick Links</h3>
                        <hr>
                        <div class="content">
                            <ul>
                                <li><a href="<?php echo $host?>/phpinfo.php">phpinfo()</a></li>
                                <li><a href="http://<?php echo $endpoint?>:8080">phpMyAdmin</a></li>
                                <li><a href="<?php echo $host?>/test_db.php">Test MySQL DB Connection</a></li>
                                <li><a href="http://<?php echo $endpoint?>:8081">Owncloud</a></li>
                                <li><a href="http://<?php echo $endpoint?>:8083">Jenkins</a></li>
                                <li><a href="http://<?php echo $endpoint?>:6080">Linux Desktop</a></li>
                                <li><a href="http://<?php echo $endpoint?>:6379">Redis</a></li>
                                <li><a href="http://<?php echo $endpoint?>:9000">Portainer</a></li>
http://45.32.165.202:9000/#!/1/docker/containers
                                <li><a href="http://<?php echo $endpoint?>:9000/#!/1/docker/containers">System management</a></li>

                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </body>
</html>