import { useState, useEffect } from 'react';

const useAuth = () => {
    const [isAuthenticated, setIsAuthenticated] = useState(false);

    useEffect(() => {
        // 检查用户是否已登录
    }, []);

    return { isAuthenticated };
};

export default useAuth;