import { useState } from 'react';
import './Auth.css';
import Footer from '../Footer';

function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    fetch('http://127.0.0.1:5555/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password }),
      credentials: 'include'
    })
      .then(res => {
        if (res.ok) {
          window.location.href = '/home';
        } else {
          return res.json().then(data => setError(data.message));
        }
      })
      .catch(err => console.error(err));
  };

  return (
    <div className="auth-container">
      <div className="auth-content">
        <div className="description-card">
          <h2>Login to Library System</h2>
          <p>
            Access your account to manage library books and records. If you don't have an account, please sign up.
          </p>
        </div>
        <div className="form-container">
          <h1>Login</h1>
          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label htmlFor="email">Email</label>
              <input
                type="email"
                id="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
              />
            </div>
            <div className="form-group">
              <label htmlFor="password">Password</label>
              <input
                type="password"
                id="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
              />
            </div>
            {error && <p className="error-message">{error}</p>}
            <button type="submit">Login</button>
          </form>
        </div>
      </div>
      <Footer />
    </div>
  );
}

export default Login;
