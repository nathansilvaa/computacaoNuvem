import axios from "axios";

// Defina a URL do backend (ajuste para o ambiente de produção)
const API_URL = "http://localhost/api/";

const api = axios.create({
  baseURL: API_URL,
});

export default api;
