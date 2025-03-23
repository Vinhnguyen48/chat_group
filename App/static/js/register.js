document.getElementById("register-btn").addEventListener("click", async function () {
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;
  const email = document.getElementById("email").value;

  try {
    const response = await fetch("/auth/register", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        username: username,
        password: password,
        email: email,
      }),
    });
    const data = await response.json();
    if (data.status === "success") {
      window.location.href = "/login";
      alert("Đăng ký thành công");
    } else {
      alert(data.error);
    }
  } catch (error) {
    console.error("Thông báo lỗi", error);
    alert("Đăng ký thất bại");
  }
});
