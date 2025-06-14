# JWT Bruteforce Tool

A simple tool for bruteforcing JWT (JSON Web Token) using wordlist to find the secret key used for signing.

## Folder Structure

```
jwt_bf/
├── jwt_bf.py          # Main script for JWT bruteforce
├── jwt.py        # Script to generate test JWT token
└── README.md          # This documentation
```

## Features

- Bruteforce JWT tokens using wordlist
- Support for HS256 algorithm (default)
- Progress bar using tqdm
- Good error handling
- Wordlist encoding using latin-1 for compatibility

## Requirements

```bash
pip install PyJWT tqdm
```

## Usage

### 1. Generate JWT Token for Testing

```bash
python jwt.py
```

This script will generate a JWT token with a predefined secret key for testing purposes.

### 2. Bruteforce JWT Token

```bash
python jwt_bf.py <jwt_token> <path_to_wordlist.txt>
```

**Parameters:**
- `jwt_token`: JWT token to bruteforce
- `path_to_wordlist.txt`: Path to wordlist file containing password list

**Example:**
```bash
python jwt_bf.py eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9... wordlist.txt
```

## Output

The tool will display:
- JWT algorithm being used
- Total number of passwords to try
- Progress bar during bruteforce process
- Secret key if found
- Decoded payload from JWT

**Example Output:**
```
[i] JWT Algorithm: HS256
[i] Total passwords to try: 10000
Bruteforcing: 45%|████▌     | 4500/10000 [00:30<00:37, 148.2it/s]

[+] Secret key found: mysecretkey
[+] Decoded payload: {'user': 'hacker', 'role': 'user'}
```

## Security Notes

⚠️ **Disclaimer**: This tool is created for educational purposes and security testing on systems that you own. Using this tool to attack systems without permission is illegal and unethical.

## Supported Algorithms

Currently the tool supports HS256 (HMAC SHA-256) algorithm. For other algorithms, you can modify the `algorithm` parameter in the `jwt_bruteforce()` function.

## Usage Tips

1. **Good Wordlist**: Use comprehensive wordlists like rockyou.txt or SecLists
2. **Resources**: Bruteforce process can take a long time depending on wordlist size
3. **Testing**: Use `jwt.py` to create JWT tokens with known secrets for testing

## Troubleshooting

**Encoding errors**: If you encounter errors while reading wordlist, make sure the wordlist file uses correct encoding. This tool uses `latin-1` encoding by default.

**JWT decode error**: Make sure the JWT token input is valid and not corrupted.

## Contributing

Please create pull requests or issues if you find bugs or want to add new features.