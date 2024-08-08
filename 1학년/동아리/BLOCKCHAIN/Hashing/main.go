package main

import (
	"crypto/sha256"
	"encoding/hex"
	"fmt"
	"strings"
)

type BansongCoinBlock struct {
	PreviousBlockHash string
	TransactionList   []string
	BlockData         string
	BlockHash         string
}

func NewBansongCoinBlock(previousBlockHash string, transactionList []string) *BansongCoinBlock {
	blockData := strings.Join(transactionList, "-") + "-" + previousBlockHash
	hash := sha256.New()
	hash.Write([]byte(blockData))
	blockHash := hex.EncodeToString(hash.Sum(nil))

	return &BansongCoinBlock{
		PreviousBlockHash: previousBlockHash,
		TransactionList:   transactionList,
		BlockData:         blockData,
		BlockHash:         blockHash,
	}
}

func main() {
	t1 := "Anna sends 2 BC to Mike"
	t2 := "Bob sends 4.1 BC to Mike"
	t3 := "Mike sends 3.2 BC to Bob"
	t4 := "Daniel sends 0.3 BC to Anna"
	t5 := "Mike sends 1 BC to Charlie"
	t6 := "Mike sends 5.4 BC to Daniel"

	initialBlock := NewBansongCoinBlock("Initial String", []string{t1, t2})
	fmt.Println(initialBlock.BlockData)
	fmt.Println(initialBlock.BlockHash)

	secondBlock := NewBansongCoinBlock(initialBlock.BlockHash, []string{t3, t4})
	fmt.Println(secondBlock.BlockData)
	fmt.Println(secondBlock.BlockHash)

	thirdBlock := NewBansongCoinBlock(secondBlock.BlockHash, []string{t5, t6})
	fmt.Println(thirdBlock.BlockData)
	fmt.Println(thirdBlock.BlockHash)
}
