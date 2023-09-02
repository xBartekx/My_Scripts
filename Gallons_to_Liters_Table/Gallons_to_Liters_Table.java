/*
Program shows conversion for gallons to liters
*/

class GalToLitTable {
	public static void main(String args[]) {

double gallons, liters;
int counter;

counter = 0;									//counter for rows


for(gallons = 1; gallons <= 100; gallons++) {
	liters = gallons * 3.7854;					//Changing gallons for liters
	System.out.println(gallons + " gallons is " + liters + " liters");
	counter++;

	if (counter == 10) {
		System.out.println();
		counter = 0;							//every 10 gallons counter is restarting 
	}
}

	
	}
}
