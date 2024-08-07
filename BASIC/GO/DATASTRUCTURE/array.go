package main

import "fmt"

func main() {
	names := [5]string{"kevin", "traveler"}
	names[2] = "alal"
	names[3] = "alal"
	names[4] = "alal"
	fmt.Println(names)
}
