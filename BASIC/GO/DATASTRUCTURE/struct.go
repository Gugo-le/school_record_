package main

import "fmt"

type person struct {
	name    string
	age     int
	favFood []string
}

func main() {
	favFood := []string{"떡볶이", "집밥"}
	kevin := person{"kevin", 18, favFood}
	fmt.Println(kevin)
}
