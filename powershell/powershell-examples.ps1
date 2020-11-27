# many examples taken directly from "PowerShell For Sysadmins" by No Starch Press
# requires PSv5 (because of Write-Host statements that use ForegroundColor and BackgroundColor
# Feb 2020
#
# Get-ExecutionPolicy
# Set-ExecutionPolicy Bypass
# Set-ExecutionPolicy Restricted

$inty = 1
$doubley = 2.5
$stringy = "stringvariable"
$booly = $true

Write-Host "variables" -ForegroundColor Black -BackgroundColor Green
$inty
$doubley
$stringy
$booly


echo ""
Write-Host "escape characters like `$ with a backtick (``)" -ForegroundColor Black -BackgroundColor Green


echo ""
Write-Host "variable types" -ForegroundColor Black -BackgroundColor Green
$inty.GetType().name
$doubley.GetType().name
$stringy.GetType().name
$booly.GetType().name


echo ""
Write-Host "cast doubley as an int" -ForegroundColor Black -BackgroundColor Green
[Int32]$doubley


echo ""
Write-Host "length of stringy" -ForegroundColor Black -BackgroundColor Green
$stringy.Length


echo ""
#Write-Host "" -ForegroundColor Black -BackgroundColor Green
#Get-Member -InputObject $inty
#Get-Member -InputObject $stringy –Name Remove


echo ""
Write-Host "substring/Remove" -ForegroundColor Black -BackgroundColor Green
$stringy.Remove(0,4)


echo ""
Write-Host "substring, the last one and two characters of the stringy variable" -ForegroundColor Black -BackgroundColor Green
$stringy.Substring($stringy.Length - 1)
$stringy.Substring($stringy.Length - 2)


echo ""
Write-Host "sequence" -ForegroundColor Black -BackgroundColor Green
1..3


echo ""
Write-Host "array" -ForegroundColor Black -BackgroundColor Green
$colorArray = @('blue','white','yellow','black')
"Array Type: " + $colorArray.GetType().name
"Array Length: " + $colorArray.Length
$colorArray
echo ""
Write-Host "individual array items" -ForegroundColor Black -BackgroundColor Green
$colorArray[0]
$colorArray[1]
$colorArray[2]
$colorArray[3]
echo ""
Write-Host "sequence of three array items" -ForegroundColor Black -BackgroundColor Green
$colorArray[0..2]
echo ""
Write-Host "append items to array" -ForegroundColor Black -BackgroundColor Green
$colorArray = $colorArray + 'orange'
$colorArray += 'purple'
$colorArray


echo ""
Write-Host "Arrays are slow because they are destroyed and re-created with every alteration" -ForegroundColor Black -BackgroundColor Green
Write-Host "ArrayList are meant to be altered, and the use .Count instead of .Length" -ForegroundColor Black -BackgroundColor Green
$colorArrayList = [System.Collections.ArrayList]@('red','white','blue')
echo ""
Write-Host "ArrayList" -ForegroundColor Black -BackgroundColor Green
"ArrayList Type: " + $colorArrayList.GetType().name
"ArrayList Count: " + $colorArrayList.Count
$colorArrayList
echo ""
Write-Host "ArrayList subslice" -ForegroundColor Black -BackgroundColor Green
$colorArrayList[0..1]
echo ""
Write-Host "add colors with .Add(), can not use += with ArrayList" -ForegroundColor Black -BackgroundColor Green
$colorArrayList.Add('gray') # immediately returns length of ArrayList before adding the new item
$colorArrayList
echo ""
Write-Host "remove colors with .Remove()" -ForegroundColor Black -BackgroundColor Green
$colorArrayList.Remove('gray')
$colorArrayList


echo ""
Write-Host "Hashtables are similar to dictionaries in Python" -ForegroundColor Black -BackgroundColor Green
$userHashtable = @{
	jsmith = 'John Smith'
	adent = 'Arthur Dent'
	zbeeblebrox = 'Zaphod Beeblebrox'
	}
$userHashtable
echo ""
Write-Host "access single hashtable item" -ForegroundColor Black -BackgroundColor Green
$userHashtable['jsmith']
echo ""
Write-Host "hashtable keys" -ForegroundColor Black -BackgroundColor Green
$userHashtable.Keys
echo ""
Write-Host "hashtable values" -ForegroundColor Black -BackgroundColor Green
$userHashtable.Values
echo ""
Write-Host "add new items using .Add(k,v) or hashtable[key]=value" -ForegroundColor Black -BackgroundColor Green
$userHashtable.Add('fprefect', 'Ford Prefect')
$userHashtable['tmcmillan'] = 'Tricia Trillian McMillan'
$userHashtable
echo ""
Write-Host "check if jsmith or mmouse key exists" -ForegroundColor Black -BackgroundColor Green
$userHashtable.ContainsKey('jsmith')
$userHashtable.ContainsKey('mmouse')


echo ""
Write-Host "create a custom object" -ForegroundColor Black -BackgroundColor Green
# instantiate
$customObject = New-Object -TypeName PSCustomObject
# fill values
$customObject = [PSCustomObject]@{SomeKeyName = 'somevalue'; SomeOtherKeyName = 'someothervalue'}
$customObject
$customObject.SomeKeyName
$customObject.SomeOtherKeyName
Get-Member -InputObject $customObject | ft


echo ""
Write-Host "comparison operators" -ForegroundColor Black -BackgroundColor Green
1 -eq 1
# eq, ne, gt, ge, lt, le, contains (for collections only), .Contains() (substrings)
2 -eq 3
"human" -contains "um" # false, cannot do substrings, only for collections
$colorArray -contains "purple" # true, working with a collection
"human".Contains("um") # true, working with substrings


echo ""
Write-Host "check if numbers are even or odd" -ForegroundColor Black -BackgroundColor Green
1..5 | % {if($_ % 2 -eq 0 ) {"$_ is even"} }
1..5 | % {if($_ % 2 -eq 1 ) {"$_ is odd"} }


$localhosts = @('127.0.0.1', '127.0.0.2', '127.0.0.3', '127.0.0.4', '127.0.0.AAAA')


echo ""
Write-Host "simple for statements " -ForegroundColor Black -BackgroundColor Green
Write-Host "	... | ForEach-Object {...}" -ForegroundColor Black -BackgroundColor Cyan
$localhosts | ForEach-Object {echo $_}
Write-Host "	foreach() method (introduced in v4)" -ForegroundColor Black -BackgroundColor Cyan
$localhosts.foreach({echo $_})


echo ""
Write-Host "foreach statement, nested if/elseif/else, regex matches, substrings" -ForegroundColor Black -BackgroundColor Green
foreach ($item in $localhosts) {
	# save last character for making comparisons inside if loops
	$lastChar = $item.Substring($item.Length - 1)
	# regex to check if digit
	if ($lastChar -match '^\d+$') {
		if ($lastChar % 2 -eq 1) {
			echo "$item ends with an odd number"
		} else {
			echo "$item ends with an even number"
		}
	# regex to check if alphabetical
	} elseif ($lastChar -match '^[a-zA-Z]+$') {
		echo "$item ends with a letter"
	} else {
		echo "$item is something else"
	}
}


echo ""
Write-Host "for loop incrementing a variable" -ForegroundColor Black -BackgroundColor Green
for ($i=0; $i -lt 5; $i++) {
	echo $i
}


echo ""
Write-Host "for loop accessing items in an array" -ForegroundColor Black -BackgroundColor Green
# one item less than the total number of items in the Array
for ($i=0; $i -lt $localhosts.Count-1; $i++) {
	echo $localhosts[$i]
}


echo ""
Write-Host "while loop incrementing a counter" -ForegroundColor Black -BackgroundColor Green
$counter = 0
while ($counter -lt 5) {
	$counter
	$counter++
}


echo ""
Write-Host "while loop with Test-Connection to a server then perform an action" -ForegroundColor Black -BackgroundColor Green
while (Test-Connection -ComputerName 127.0.0.1 -Quiet -Count 1) {
	echo "do a thing when a connection is able to be established"
	break
}


echo ""
Write-Host "do until loop" -ForegroundColor Black -BackgroundColor Green
do {
	$choice = Read-Host -Prompt "type ps: "
} until ($choice -eq "ps")
Write-Host -Object "you typed ps"


echo ""
Write-Host "try/catch/finally to handle errors" -ForegroundColor Black -BackgroundColor Green
Write-Host "error actions: Continue/Ignore/Inquire/SilentlyContinue/Stop" -ForegroundColor Black -BackgroundColor Green
$fakePath = ".\DoesNotExistAtAll"
try {
	$files = gci -Path $fakePath -ErrorAction Stop
	$files.foreach({
		$fileContent = gc $files
		$fileContent[0]
	})
} catch {
	$_.Exception.Message
}


echo ""
Write-Host "make a function then call it" -ForegroundColor Black -BackgroundColor Green
# Get-Command -CommandType Function
function MakeTaco {Write-Host 'Made a taco!'}
MakeTaco


echo ""
Write-Host "make a function that optionally takes a parameter" -ForegroundColor Black -BackgroundColor Green
function OrderTaco {
	[CmdletBinding()]
	param(
		[Parameter()]
		[string] $Quantity
	)
	Write-Host "Ordering $Quantity tacos."
}
echo "running command:  OrderTaco -Quantity 5"
OrderTaco
OrderTaco -Quantity 5


echo ""
Write-Host "make a function that requires a parameter" -ForegroundColor Black -BackgroundColor Green
function ForceOrderTaco {
	[CmdletBinding()]
	param(
		[Parameter(Mandatory)]
		[string] $Quantity
	)
	Write-Host "Certainly ordering $Quantity tacos."
}
echo "running command:  ForceOrderTaco (will prompt for a quantity)"
ForceOrderTaco
echo "running command:  ForceOrderTaco -Quantity 5"
ForceOrderTaco -Quantity 5


echo ""
Write-Host "make a function that requires a parameter but has a default" -ForegroundColor Black -BackgroundColor Green
function DefaultOrderTaco {
	[CmdletBinding()]
	param(
		[Parameter(Mandatory)]
		[string] $Quantity = 1
	)
	Write-Host "Ordering $Quantity tacos (default: 1)."
}
echo "running command:  DefaultOrderTaco (may pass a quantity)"
DefaultOrderTaco
echo "running command:  DefaultOrderTaco -Quantity 5"
DefaultOrderTaco -Quantity 5


echo ""
Write-Host "make a function that validates input" -ForegroundColor Black -BackgroundColor Green
function ValidOrderTaco {
	[CmdletBinding()]
	param(
		[Parameter(Mandatory)]
		[ValidateSet('1','2','3','4','5','6','7','8','9','10')]
		[string] $Quantity = 1
	)
	Write-Host "Ordering $Quantity tacos (default: 1)."
}
echo "running command:  ValidOrderTaco (may pass a quantity)"
ValidOrderTaco
echo "running command:  ValidOrderTaco -Quantity 5"
ValidOrderTaco -Quantity 5
echo "running command which will produce an error:  ValidOrderTaco -Quantity 11"
ValidOrderTaco -Quantity 11


echo ""
echo "make a function that accepts pipeline input:"
echo "	`$tacoShells = @('Crunchy', 'Soft', 'Invisible')"
echo "	`$tacoShells | OrderManyTacos -Quantity 10"
Write-Host "	Invisible taco will cause an error!" -ForegroundColor Black -BackgroundColor Red
function OrderManyTacos {
	[CmdletBinding()]
	param(
		[Parameter(Mandatory)]
		[ValidateSet(1,2,3,4,5,6,7,8,9,10)]
		[int] $Quantity,
		# need comma between every set of parameters
		[Parameter(Mandatory, ValueFromPipeline)]
		[ValidateSet('Crunchy', 'Soft')]
		[string] $Shell
	)
	# process is where the function's actions take place
	process {
		Write-Host "Ordering $Quantity $Shell taco(s)."
	}
}
$tacoShells = @('Crunchy', 'Soft', 'Invisible')
$tacoShells | OrderManyTacos -Quantity 10


echo ""
Write-Host "colorized output (introduced in v5)" -ForegroundColor Black -BackgroundColor Green
Write-Host "valid options for -ForegroundColor and -BackgroundColor:  Black DarkBlue DarkGreen DarkCyan DarkRed DarkMagenta DarkYellow Gray DarkGray Blue Green Cyan Red Magenta Yellow White" -ForegroundColor Black -BackgroundColor Green
$bgColors = @('Black', 'DarkBlue', 'DarkGreen', 'DarkCyan', 'DarkRed', 'DarkMagenta', 'DarkYellow', 'Gray', 'DarkGray', 'Blue', 'Green', 'Cyan', 'Red', 'Magenta', 'Yellow', 'White')
$bgColors.foreach({Write-Host "Black text on $_ background" -ForegroundColor Black -BackgroundColor $_})
$fgColors = @('Black', 'DarkBlue', 'DarkGreen', 'DarkCyan', 'DarkRed', 'DarkMagenta', 'DarkYellow', 'Gray', 'DarkGray', 'Blue', 'Green', 'Cyan', 'Red', 'Magenta', 'Yellow', 'White')
$fgColors.foreach({Write-Host "$_ text on White background" -ForegroundColor $_ -BackgroundColor White})


echo ""
Write-Host "make a function that produces simple output headers" -ForegroundColor Black -BackgroundColor Green
function SectionHeaderMessage {
	[CmdletBinding()]
	param(
		[Parameter(Mandatory)]
		[string] $Message
	)
	Write-Host "$Message" -ForegroundColor Cyan -BackgroundColor DarkRed
}
SectionHeaderMessage -Message "This Is Text Passed Through A Function"


# TODO
# error handling notes
# reading from / writing to JSON and CSV files
# $output = Invoke-WebRequest -Uri "https://www.google.com"
# $output.Content
