export interface Task {
  id: number;
  user_id: number;
  title: string;
  priority: 'LOW' | 'MEDIUM' | 'HIGH';
}

export interface TaskCreate {
  user_id?: number;
  title: string;
  priority: 'LOW' | 'MEDIUM' | 'HIGH';
}

export interface TaskUpdate {
  title?: string;
  priority?: 'LOW' | 'MEDIUM' | 'HIGH';
}

export interface LoginCredentials {
  username: string;
  password: string;
}

export interface AuthResponse {
  access_token: string;
  token_type: string;
}

export interface UserCreate {
  username: string;
  email: string;
  password: string;
} 