<?php
						$name = $_GET["s_name"];
						$s0 = $_GET["s_zero"];
						$round = $_GET["rounds"];
						$t = $_GET["t"];
						$alpha = $_GET["alpha"];
						$theta = $_GET["theta"];
						$sd = $_GET["sd"];
						$miu = $_GET["miu"];
										
						fclose($f);

						$execute = "python ./models/monte_carlo/script.py ";
						$execute = $execute.
						exec($execute);
						$s = file_get_contents($out_file_name);
						echo $s;
						?>