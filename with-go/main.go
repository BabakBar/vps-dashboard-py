package main

import (
	"encoding/json"
	"log"
	"math"
	"os"
	"time"

	"github.com/shirou/gopsutil/v3/cpu"
	"github.com/shirou/gopsutil/v3/disk"
	"github.com/shirou/gopsutil/v3/mem"
)

type Metrics struct {
	CPUUsagePercent  float64 `json:"cpu_usage_percent"`
	RAMUsagePercent  float64 `json:"ram_usage_percent"`
	DiskUsagePercent float64 `json:"disk_usage_percent"`
}

func main() {
	var metrics Metrics

	// Get CPU usage
	cpuPercent, err := cpu.Percent(time.Second, false)
	if err != nil {
		log.Printf("Error getting CPU usage: %v", err)
		return
	}
	metrics.CPUUsagePercent = math.Round(cpuPercent[0]*100) / 100

	// Get RAM usage
	memInfo, err := mem.VirtualMemory()
	if err != nil {
		log.Printf("Error getting memory usage: %v", err)
		return
	}
	metrics.RAMUsagePercent = math.Round(memInfo.UsedPercent*100) / 100

	// Get disk usage
	diskInfo, err := disk.Usage("/")
	if err != nil {
		log.Printf("Error getting disk usage: %v", err)
		return
	}
	metrics.DiskUsagePercent = math.Round(diskInfo.UsedPercent*100) / 100

	// Marshal to JSON
	jsonData, err := json.MarshalIndent(metrics, "", "  ")
	if err != nil {
		log.Printf("Error marshaling to JSON: %v", err)
		return
	}

	// Create timestamped filename
	filename := "health_" + time.Now().Format("2006-01-02_15-04-05") + ".json"

	// Write JSON to file
	err = os.WriteFile(filename, jsonData, 0644)
	if err != nil {
		log.Printf("Error writing to file: %v", err)
		return
	}

	log.Printf("Metrics saved to %s", filename)
}
