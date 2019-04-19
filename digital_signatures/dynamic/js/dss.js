function hash() {
    val = document.getElementById('input').value
    console.log(val)
    fetch("/api/hash?val="+val)
        .then(res => res.json())
        .then(res => {
            document.getElementById('hash_value').value = res.hash;
        });
  }

function set_1024f4(){
    fetch("/api/generate?sz=1024&e=0")
    .then(res => res.json())
        .then(res => {
            document.rsatest.n.value=res.key;
            document.rsatest.e.value=res.e;
        });
}
function set_1024e3(){
    fetch("/api/generate?sz=1024&e=3")
    .then(res => res.json())
        .then(res => {
            document.rsatest.n.value=res.key;
            document.rsatest.e.value=res.e;
        });
}
function set_512e3(){
    fetch("/api/generate?sz=512&e=3")
    .then(res => res.json())
        .then(res => {
            document.rsatest.n.value=res.key;
            document.rsatest.e.value=res.e;
        });
}
function set_512f4(){
    fetch("/api/generate?sz=512&e=0")
    .then(res => res.json())
        .then(res => {
            document.rsatest.n.value=res.key;
            document.rsatest.e.value=res.e;
        });
}
function do_encrypt(){
    if(document.getElementById('hash_value').value != document.rsatest.plaintext.value) {
        alert("Hash output and input to RSA should be same!");
        return;
    }
    if(document.rsatest.n.value == ''){
        alert("Generate RSA Public Key First!")
        return;
    }
    h = document.rsatest.plaintext.value;
    var before = new Date();
    fetch('/api/encrypt?h='+h)
    .then(res => res.json())
    .then(res => {
        let after = new Date()
        document.rsatest.ciphertext.value = res.ds;
        document.rsatest.cipherb64.value = res.ds64;
        document.rsatest.status.value = "Time: " + (after - before) + "ms";
    });
}