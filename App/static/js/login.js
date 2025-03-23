document.getElementById("login-btn").addEventListener("click",async function(){
    const username=document.getElementById("username").value;
    const password=document.getElementById("password").value;

    try {
        const response=await fetch("/auth/login",{
            method:"POST",
            headers:{
                "Content-Type":"application/json"
            },
            body:JSON.stringify({
                username:username,
                password:password
            })
        });
        const data=await response.json();
        if (data.ok){
            alert("Đăng nhập thành công");
            location.href="/group_chat";
        }
        else
        {
            alert(data.message);
        }

    }catch(error){
        console.error("Thông báo lỗi",error);
        alert("Đăng nhập thất bại");
    }
});