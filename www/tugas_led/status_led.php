<?php
$host = "localhost";
$user = "root";
$password = "";
$database = "tugas_led";

// Buat koneksi ke database
$conn = new mysqli($host, $user, $password, $database);

// Cek koneksi
if ($conn->connect_error) {
    die("Koneksi gagal: " . $conn->connect_error);
}

// Query untuk mengambil status LED terbaru
$sql = "SELECT kondidisi FROM dataled ORDER BY id DESC LIMIT 1";
$result = $conn->query($sql);

$status_led = 0; // Default OFF
if ($result->num_rows > 0) {
    // Ambil hasil
    $row = $result->fetch_assoc();
    $status_led = $row['kondidisi'];
}

// Tutup koneksi
$conn->close();

// Mengembalikan status LED
echo json_encode(['status' => $status_led]);
?>
