# arq

Basic ARQ system written in Python

## Usage

To use the project, execute the following :

```bash
python main.py --probability float --data_size int --package_size int --parity_bits int --connection_type int
```

### Parameters

* probability :  Probability of bit toggling
* data_size : Size of the data to generate (in bytes)
* package_size : Size of the package data in range [5,7] (in bits)
* parity_bits : Amount of parity bits
* connection_type : The type of the connection to use in range [1,2], where :
	* 1 - is bidirectional noisy connection based on random flipping the bits with the given probability
	* 2- is bidirectional symmetric connection, based on the komm module for Python