import hmac, hashlib, json, base64, time

key_b64 = "BAdHRolSnc/fSiVf30YaHrqinxqLKEJw4/0LsC5wXwFv3SJhS7TdoO04IQT2jtRKOwWaG4x2/MBzttoTNmuoj20="
key = base64.b64decode(key_b64)  # Decode key to bytes for HMAC

# 🕒 Generate dynamic Unix timestamp (in seconds)
ts = str(int(time.time()))

# 🔏 Create a secure HMAC-SHA512 signature based on the timestamp
message = ts.encode()
signature = hmac.new(key, message, hashlib.sha512).hexdigest()
ts_sign = f"ts.1.{signature}"  # Final signature token with prefix

# 📦 Build request payload structure
data = {
    "req_content": "ticket,path,timestamp",        # Request components being signed
    "req_sign": "MEQCIG8lr/48WEHfwT9fgITaNX6lgEGUoKpcYJC19f1/0bsDAiA55KFnubhjAi9sfPDnkn4Pan68zVV6lbYuPeyvpIV8cw==",  # Static signature (placeholder)
    "timestamp": ts,                                # Matching timestamp used for signing
    "ts_sign": ts_sign                              # The generated HMAC value
}

# 🔄 Minify JSON and Base64-encode for use as a secure token (e.g., in request headers)
json_data = json.dumps(data, separators=(',', ':'))
token = base64.b64encode(json_data.encode()).decode()

print(token)
