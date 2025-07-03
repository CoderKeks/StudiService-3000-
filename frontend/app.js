async function loadStudierende() {
    try {
      const response = await fetch('http://127.0.0.1:5001/api/studierende');
      if (!response.ok) {
        throw new Error(`Fehler beim Laden der Daten: ${response.status} ${response.statusText}`);
      }
      const studierende = await response.json();
  
      const tbody = document.querySelector('#studierendeTable tbody');
      tbody.innerHTML = ''; // Tabelle leeren
  
      studierende.forEach(s => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td>${s.id}</td>
          <td>${s.name}</td>
          <td>${s.matrikelnummer}</td>
          <td>${s.studiengang}</td>
        `;
        tbody.appendChild(tr);
      });
    } catch (error) {
      alert(error.message);
      console.error(error);
    }
  }
  
  window.addEventListener('load', loadStudierende);
  