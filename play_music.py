import pygame
import time
import threading

def play_music(file_path):
    # Inisialisasi mixer Pygame
    pygame.mixer.init()
    print("Memulai pemutaran musik...")
    
    # Memuat file musik
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    
    # Menjalankan thread untuk mengelola input pengguna
    control_thread = threading.Thread(target=music_controls)
    control_thread.start()
    
    # Tunggu hingga musik selesai diputar
    while pygame.mixer.music.get_busy():
        time.sleep(1)
    
    print("Pemutaran selesai.")

def music_controls():
    while pygame.mixer.music.get_busy():
        print("\nKontrol Musik:")
        print("1. Pause")
        print("2. Resume")
        print("3. Stop")
        print("4. Volume Up")
        print("5. Volume Down")
        print("6. Exit")
        
        try:
            choice = int(input("Pilih opsi: "))
            if choice == 1:
                pygame.mixer.music.pause()
                print("Musik di-pause.")
            elif choice == 2:
                pygame.mixer.music.unpause()
                print("Melanjutkan musik.")
            elif choice == 3:
                pygame.mixer.music.stop()
                print("Musik dihentikan.")
                break
            elif choice == 4:
                volume = pygame.mixer.music.get_volume()
                pygame.mixer.music.set_volume(min(volume + 0.1, 1.0))
                print(f"Volume dinaikkan ke: {pygame.mixer.music.get_volume():.2f}")
            elif choice == 5:
                volume = pygame.mixer.music.get_volume()
                pygame.mixer.music.set_volume(max(volume - 0.1, 0.0))
                print(f"Volume diturunkan ke: {pygame.mixer.music.get_volume():.2f}")
            elif choice == 6:
                print("Keluar dari kontrol.")
                break
            else:
                print("Pilihan tidak valid. Coba lagi.")
        except ValueError:
            print("Masukkan angka yang valid.")

if __name__ == "__main__":
    # Ganti "musik.mp3" dengan nama file musik Anda
    file_path = "musik.mp3"
    try:
        play_music(file_path)
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
