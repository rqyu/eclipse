<?include 'header.php'?>


<div id="eclipse_main">

	<div id="eclipse_center">
		<form id="monte_carlo" method="GET" action="monte.php">
			<table align="center">
				<tr><td colspan=2 align="center"><b>Please enter the following values</b></td></tr>
				<tr>
					<td>Name</td><td><input type="text" name="s_name" value="RIMM" /></td>
				</tr>
				<tr>
					<td>S0</td><td><input type="text" name="s_zero" value=16 /></td>
				</tr>
				<tr>
					<td>R</td><td><input type="text" name="rounds" value=1000 /></td>
				</tr>
				<tr>
					<td>t</td><td><input type="text" name="t" value=1 /></td>
				</tr>
				<tr>
					<td>miu</td><td><input type="text" name="miu" value=0.1 /></td>
				</tr>
				<tr>
					<td>sigma</td><td><input type="text" name="sd" value=0.02 /></td>
				</tr>
				<tr>
					<td>alpha</td><td><input type="text" name="alpha" value=0.2 /></td>
				</tr>
				<tr>
					<td>theta</td><td><input type="text" name="theta" value=0.02 /></td>
				</tr>
				<tr>
					<td><input type="submit" value="Simulate!"></td>
					<td><input type="reset" value="Reset Fields"></td>
				</tr>
			</table>
		</form>
	</div>
	
	<div id="eclipse_right">
		<table align="center">
			<tr><td><i>Instruction</i></td></tr>
			<tr><td><b>Name:</b> Name or ticker of your stock</td></tr>
			<tr><td><b>S0:</b> Stock price at time 0</td></tr>
			<tr><td><b>R:</b> Number of simulations you want</td></tr>
			<tr><td><b>t:</b> time-units after current time(S1,S2..)</td></tr>
			<tr><td><b>miu:</b> Lognormal distribution mean</td></tr>
			<tr><td><b>sigma:</b> Lognormal distribution standard deviation</td></tr>
			<tr><td><b>alpha:</b> the stock's continuously annual compounded rate of return</td></tr>
			<tr><td><b>theta:</b> the stock's continuous annual divident rate</td></tr>
			<tr><td>All fields can be entered single value(eg. 40) or comma seperated values(eg. 40,50,40)</td></tr>
		</table>
	</div>
	
<!--	
NASDAQ:	JKHY
NASDAQ:	SLP
NASDAQ:	MLAB
FDS
FEIC
NASDAQ: ASMI
NASDAQ: MELI
NASDAQ: SYNT
NYSE:	MR

Final:
ASMI
EBIX
FEIC
MELI
MLAB
MR
SLP
SYNT
-->
</div>


<?include 'footer.php'?>