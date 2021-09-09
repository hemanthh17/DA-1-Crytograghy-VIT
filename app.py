from flask import Flask, render_template,url_for,request,redirect,flash
app=Flask(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
def generateKey(string, key):
	key = list(key)
	if len(string) == len(key):
		return(key)
	else:
		for i in range(len(string) -
					len(key)):
			key.append(key[i % len(key)])
	return("" . join(key))
	
# This function returns the
# encrypted text generated
# with the help of the key
def cipherText(string, key):
	cipher_text = []
	for i in range(len(string)):
		x = (ord(string[i]) +
			ord(key[i])) % 26
		x += ord('A')
		cipher_text.append(chr(x))
	return("" . join(cipher_text))
	
# This function decrypts the
# encrypted text and returns
# the original text
def originalText(cipher_text, key):
	orig_text = []
	for i in range(len(cipher_text)):
		x = (ord(cipher_text[i]) -
			ord(key[i]) + 26) % 26
		x += ord('A')
		orig_text.append(chr(x))
	return("" . join(orig_text))

@app.route('/',methods=['GET','POST'])
def welcome():
    if request.method=='POST':
        word=str(request.form['data'])
        keyw=str(request.form['key'])
        enc= str(request.form['option'])
        key = generateKey(word, keyw)
        if enc=='encrypt':
            cipher_text=cipherText(word,key)
            flash('The data was encrypted and the output is'+' '+cipher_text)
            return render_template('index1.html')
        else:
            original_text=originalText(word,key)
            flash('The data was decrypted and the output is'+' '+original_text)
            return render_template('index1.html')
    
        
        
        
    return render_template('index1.html',form=request.form)

    
    
        
if __name__=="__main__":
    app.run(debug=True)