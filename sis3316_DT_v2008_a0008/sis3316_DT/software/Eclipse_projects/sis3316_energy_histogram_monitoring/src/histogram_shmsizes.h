// shmsizes.h
// sizes for shared memory sections

// 16 MByte
#define SHM_NOF_CHANNELS 						16
#define SHM_ENERGY_HISTOGRAM_CHANNEL_OFFSET		0x10000	// 64K x 32-bit
#define SHM_ENERGY_HISTOGRAM_SIZE 				4 * 2 * SHM_NOF_CHANNELS * SHM_ENERGY_HISTOGRAM_CHANNEL_OFFSET   //  SIS3316 Online and PC histograms (bytes)

#define SHM_SIS3316_HISTOGRAM_OFFSET 			0x0
#define SHM_PC_HISTOGRAM_OFFSET 				SHM_NOF_CHANNELS * SHM_ENERGY_HISTOGRAM_CHANNEL_OFFSET


