-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Tempo de geração: 27-Jun-2023 às 01:31
-- Versão do servidor: 5.7.36
-- versão do PHP: 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `brutus`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `carros`
--

DROP TABLE IF EXISTS `carros`;
CREATE TABLE IF NOT EXISTS `carros` (
  `id` int(6) NOT NULL AUTO_INCREMENT,
  `chassi` text NOT NULL,
  `cor` text NOT NULL,
  `km` int(11) NOT NULL,
  `ano` int(4) NOT NULL,
  `modelo` text NOT NULL,
  `custo` int(11) NOT NULL,
  `preco` int(11) NOT NULL,
  `qt` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=51 DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `carros`
--

INSERT INTO `carros` (`id`, `chassi`, `cor`, `km`, `ano`, `modelo`, `custo`, `preco`, `qt`) VALUES
(3, 'IJKL9012', 'Azul', 8000, 2019, 'Corolla', 28000, 32000, 1),
(2, 'EFGH5678', 'Preto', 10000, 2017, 'Civic', 25000, 30000, 2),
(1, 'ABCD1234', 'Prata', 5000, 2018, 'Fusion', 30000, 35000, 1),
(4, 'MNOP3456', 'Vermelho', 6000, 2018, 'Golf', 22000, 27000, 3),
(5, 'QRST7890', 'Branco', 12000, 2016, 'Cruze', 18000, 24000, 2),
(6, 'UVWX1234', 'Prata', 9000, 2019, 'HR-V', 26000, 30000, 1),
(7, 'YZAB5678', 'Preto', 11000, 2017, 'Civic', 24000, 28000, 2),
(8, 'CDEF9012', 'Azul', 7500, 2019, 'Corolla', 27000, 31000, 1),
(9, 'GHIJ3456', 'Vermelho', 5500, 2018, 'Golf', 21000, 26000, 3),
(10, 'KLMN7890', 'Branco', 11500, 2016, 'Cruze', 17000, 23000, 2),
(11, 'OPQR1234', 'Prata', 8500, 2019, 'HR-V', 25000, 29000, 1),
(12, 'STUV5678', 'Preto', 10500, 2017, 'Civic', 23000, 27000, 2),
(13, 'WXYZ9012', 'Azul', 7000, 2019, 'Corolla', 26000, 30000, 1),
(14, 'BCDE3456', 'Vermelho', 5000, 2018, 'Golf', 20000, 25000, 3),
(15, 'FGHI7890', 'Branco', 11000, 2016, 'Cruze', 16000, 22000, 2),
(16, 'JKLM1234', 'Prata', 8000, 2019, 'HR-V', 24000, 28000, 1),
(17, 'NOPQ5678', 'Preto', 10000, 2017, 'Civic', 22000, 26000, 2),
(18, 'RSTU9012', 'Azul', 7000, 2019, 'Corolla', 25000, 29000, 1),
(19, 'VWXY3456', 'Vermelho', 4500, 2018, 'Golf', 19000, 24000, 3),
(20, 'ZABC7890', 'Branco', 10500, 2016, 'Cruze', 15000, 21000, 2),
(21, 'DEFG1234', 'Prata', 7500, 2019, 'HR-V', 23000, 27000, 1),
(22, 'HIJK5678', 'Preto', 9500, 2017, 'Civic', 21000, 25000, 2),
(23, 'LMNO9012', 'Azul', 6500, 2019, 'Corolla', 24000, 28000, 1),
(24, 'PQRS3456', 'Vermelho', 4000, 2018, 'Golf', 18000, 23000, 3),
(25, 'TUVW7890', 'Branco', 10000, 2016, 'Cruze', 14000, 20000, 2),
(26, 'WXYZ1234', 'Prata', 7000, 2019, 'HR-V', 22000, 26000, 1),
(27, 'BCDE5678', 'Preto', 9000, 2017, 'Civic', 20000, 24000, 2),
(28, 'FGHI9012', 'Azul', 6000, 2019, 'Corolla', 23000, 27000, 1),
(29, 'JKLM3456', 'Vermelho', 3500, 2018, 'Golf', 17000, 22000, 3),
(30, 'NOPQ7890', 'Branco', 9500, 2016, 'Cruze', 13000, 19000, 2),
(31, 'RSTU1234', 'Prata', 7000, 2019, 'HR-V', 21000, 25000, 1),
(32, 'VWXY5678', 'Preto', 8500, 2017, 'Civic', 19000, 23000, 2),
(33, 'ZABCD9012', 'Azul', 5500, 2019, 'Corolla', 22000, 26000, 1),
(34, 'EFGH3456', 'Vermelho', 3000, 2018, 'Golf', 16000, 21000, 3),
(35, 'IJKL7890', 'Branco', 9000, 2016, 'Cruze', 12000, 18000, 2),
(36, 'MNOP1234', 'Prata', 6500, 2019, 'HR-V', 20000, 24000, 1),
(37, 'QRST5678', 'Preto', 8000, 2017, 'Civic', 18000, 22000, 2),
(38, 'UVWX9012', 'Azul', 5000, 2019, 'Corolla', 21000, 25000, 1),
(39, 'YZAB3456', 'Vermelho', 2500, 2018, 'Golf', 15000, 20000, 3),
(40, 'CDEF7890', 'Branco', 8500, 2016, 'Cruze', 11000, 17000, 2),
(41, 'GHIJ1234', 'Prata', 6000, 2019, 'HR-V', 19000, 23000, 1),
(42, 'KLMN5678', 'Preto', 7500, 2017, 'Civic', 17000, 21000, 2),
(43, 'OPQR9012', 'Azul', 4500, 2019, 'Corolla', 20000, 24000, 1),
(44, 'STUV3456', 'Vermelho', 2000, 2018, 'Golf', 14000, 19000, 3),
(45, 'WXYZ7890', 'Branco', 8000, 2016, 'Cruze', 10000, 16000, 2),
(46, 'BCDE1234', 'Prata', 5500, 2019, 'HR-V', 18000, 22000, 1),
(47, 'FGHI5678', 'Preto', 7000, 2017, 'Civic', 16000, 20000, 2),
(48, 'JKLM9012', 'Azul', 4000, 2019, 'Corolla', 19000, 23000, 1),
(49, 'NOPQ3456', 'Vermelho', 1500, 2018, 'Golf', 13000, 18000, 3),
(50, 'RSTU7890', 'Branco', 7500, 2016, 'Cruze', 9000, 15000, 2);

-- --------------------------------------------------------

--
-- Estrutura da tabela `clientes`
--

DROP TABLE IF EXISTS `clientes`;
CREATE TABLE IF NOT EXISTS `clientes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` text NOT NULL,
  `idade` int(11) NOT NULL,
  `cpf` text NOT NULL,
  `endereco` text NOT NULL,
  `cidade` text NOT NULL,
  `cep` text NOT NULL,
  `telefone` text NOT NULL,
  `email` text NOT NULL,
  `sexo` text NOT NULL,
  `qtCompras` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=51 DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `clientes`
--

INSERT INTO `clientes` (`id`, `nome`, `idade`, `cpf`, `endereco`, `cidade`, `cep`, `telefone`, `email`, `sexo`, `qtCompras`) VALUES
(1, 'João Silva', 35, '123.456.789-00', 'Rua A, 123', 'São Paulo', '01234-567', '(11) 1234-5678', 'joao.silva@example.com', 'Masculino', 5),
(2, 'Maria Souza', 28, '987.654.321-00', 'Avenida B, 456', 'Rio de Janeiro', '23456-789', '(21) 2345-6789', 'maria.souza@example.com', 'Feminino', 3),
(3, 'Pedro Santos', 42, '456.789.123-00', 'Rua C, 789', 'Belo Horizonte', '34567-890', '(31) 3456-7890', 'pedro.santos@example.com', 'Masculino', 7),
(4, 'Ana Oliveira', 31, '654.321.987-00', 'Avenida D, 012', 'Brasília', '45678-901', '(61) 4567-8901', 'ana.oliveira@example.com', 'Feminino', 2),
(5, 'Carlos Rodrigues', 39, '987.123.456-00', 'Rua E, 345', 'Salvador', '56789-012', '(71) 5678-9012', 'carlos.rodrigues@example.com', 'Masculino', 4),
(6, 'Mariana Costa', 25, '321.456.789-00', 'Avenida F, 678', 'Recife', '67890-123', '(81) 6789-0123', 'mariana.costa@example.com', 'Feminino', 1),
(7, 'Fernando Gomes', 47, '789.321.654-00', 'Rua G, 901', 'Porto Alegre', '78901-234', '(51) 7890-1234', 'fernando.gomes@example.com', 'Masculino', 6),
(8, 'Amanda Almeida', 33, '654.987.321-00', 'Avenida H, 1234', 'Curitiba', '89012-345', '(41) 8901-2345', 'amanda.almeida@example.com', 'Feminino', 3),
(9, 'Ricardo Lima', 37, '321.789.654-00', 'Rua I, 5678', 'Fortaleza', '90123-456', '(85) 9012-3456', 'ricardo.lima@example.com', 'Masculino', 2),
(10, 'Patrícia Castro', 29, '789.654.321-00', 'Avenida J, 9012', 'Manaus', '01234-567', '(92) 0123-4567', 'patricia.castro@example.com', 'Feminino', 4),
(11, 'José Santos', 41, '654.123.789-00', 'Rua K, 3456', 'São Paulo', '12345-678', '(11) 2345-6789', 'jose.santos@example.com', 'Masculino', 5),
(12, 'Camila Fernandes', 27, '987.789.321-00', 'Avenida L, 6789', 'Rio de Janeiro', '23456-789', '(21) 3456-7890', 'camila.fernandes@example.com', 'Feminino', 3),
(13, 'Gustavo Lima', 39, '321.654.987-00', 'Rua M, 0123', 'Belo Horizonte', '34567-890', '(31) 4567-8901', 'gustavo.lima@example.com', 'Masculino', 7),
(14, 'Carolina Oliveira', 32, '789.987.654-00', 'Avenida N, 4567', 'Brasília', '45678-901', '(61) 5678-9012', 'carolina.oliveira@example.com', 'Feminino', 2),
(15, 'Rafael Rodrigues', 38, '654.321.789-00', 'Rua O, 8901', 'Salvador', '56789-012', '(71) 6789-0123', 'rafael.rodrigues@example.com', 'Masculino', 4),
(16, 'Vanessa Costa', 26, '987.789.123-00', 'Avenida P, 2345', 'Recife', '67890-123', '(81) 7890-1234', 'vanessa.costa@example.com', 'Feminino', 1),
(17, 'Marcelo Gomes', 45, '321.987.456-00', 'Rua Q, 5678', 'Porto Alegre', '78901-234', '(51) 8901-2345', 'marcelo.gomes@example.com', 'Masculino', 6),
(18, 'Bianca Almeida', 31, '789.321.987-00', 'Avenida R, 9012', 'Curitiba', '89012-345', '(41) 9012-3456', 'bianca.almeida@example.com', 'Feminino', 3),
(19, 'Leonardo Lima', 36, '321.654.789-00', 'Rua S, 1234', 'Fortaleza', '90123-456', '(85) 0123-4567', 'leonardo.lima@example.com', 'Masculino', 2),
(20, 'Fernanda Castro', 30, '789.987.654-00', 'Avenida T, 5678', 'Manaus', '01234-567', '(92) 2345-6789', 'fernanda.castro@example.com', 'Feminino', 4),
(21, 'Luiz Silva', 40, '654.123.987-00', 'Rua U, 9012', 'São Paulo', '12345-678', '(11) 3456-7890', 'luiz.silva@example.com', 'Masculino', 5),
(22, 'Mariana Fernandes', 24, '987.789.123-00', 'Avenida V, 2345', 'Rio de Janeiro', '23456-789', '(21) 4567-8901', 'mariana.fernandes@example.com', 'Feminino', 3),
(23, 'Gustavo Santos', 38, '321.654.987-00', 'Rua W, 5678', 'Belo Horizonte', '34567-890', '(31) 5678-9012', 'gustavo.santos@example.com', 'Masculino', 7),
(24, 'Carolina Oliveira', 30, '789.987.654-00', 'Avenida X, 9012', 'Brasília', '45678-901', '(61) 6789-0123', 'carolina.oliveira@example.com', 'Feminino', 2),
(25, 'Rafael Rodrigues', 37, '654.321.789-00', 'Rua Y, 1234', 'Salvador', '56789-012', '(71) 7890-1234', 'rafael.rodrigues@example.com', 'Masculino', 4),
(26, 'Vanessa Costa', 25, '987.789.123-00', 'Avenida Z, 2345', 'Recife', '67890-123', '(81) 9012-3456', 'vanessa.costa@example.com', 'Feminino', 1),
(27, 'Marcelo Gomes', 44, '321.987.456-00', 'Rua AA, 5678', 'Porto Alegre', '78901-234', '(51) 0123-4567', 'marcelo.gomes@example.com', 'Masculino', 6),
(28, 'Bianca Almeida', 30, '789.321.987-00', 'Avenida BB, 9012', 'Curitiba', '89012-345', '(41) 2345-6789', 'bianca.almeida@example.com', 'Feminino', 3),
(29, 'Leonardo Lima', 35, '321.654.789-00', 'Rua CC, 1234', 'Fortaleza', '90123-456', '(85) 3456-7890', 'leonardo.lima@example.com', 'Masculino', 2),
(30, 'Fernanda Castro', 29, '789.987.654-00', 'Avenida DD, 5678', 'Manaus', '01234-567', '(92) 4567-8901', 'fernanda.castro@example.com', 'Feminino', 4),
(31, 'Luiz Silva', 39, '654.123.987-00', 'Rua EE, 9012', 'São Paulo', '12345-678', '(11) 5678-9012', 'luiz.silva@example.com', 'Masculino', 5),
(32, 'Mariana Fernandes', 23, '987.789.123-00', 'Avenida FF, 2345', 'Rio de Janeiro', '23456-789', '(21) 6789-0123', 'mariana.fernandes@example.com', 'Feminino', 3),
(33, 'Gustavo Santos', 37, '321.654.987-00', 'Rua GG, 5678', 'Belo Horizonte', '34567-890', '(31) 7890-1234', 'gustavo.santos@example.com', 'Masculino', 7),
(34, 'Carolina Oliveira', 29, '789.987.654-00', 'Avenida HH, 9012', 'Brasília', '45678-901', '(61) 8901-2345', 'carolina.oliveira@example.com', 'Feminino', 2),
(35, 'Rafael Rodrigues', 36, '654.321.789-00', 'Rua II, 1234', 'Salvador', '56789-012', '(71) 9012-3456', 'rafael.rodrigues@example.com', 'Masculino', 4),
(36, 'Vanessa Costa', 24, '987.789.123-00', 'Avenida JJ, 2345', 'Recife', '67890-123', '(81) 0123-4567', 'vanessa.costa@example.com', 'Feminino', 1),
(37, 'Marcelo Gomes', 43, '321.987.456-00', 'Rua KK, 5678', 'Porto Alegre', '78901-234', '(51) 2345-6789', 'marcelo.gomes@example.com', 'Masculino', 6),
(38, 'Bianca Almeida', 29, '789.321.987-00', 'Avenida LL, 9012', 'Curitiba', '89012-345', '(41) 3456-7890', 'bianca.almeida@example.com', 'Feminino', 3),
(39, 'Leonardo Lima', 34, '321.654.789-00', 'Rua MM, 1234', 'Fortaleza', '90123-456', '(85) 4567-8901', 'leonardo.lima@example.com', 'Masculino', 2),
(40, 'Fernanda Castro', 28, '789.987.654-00', 'Avenida NN, 5678', 'Manaus', '01234-567', '(92) 5678-9012', 'fernanda.castro@example.com', 'Feminino', 4),
(41, 'Luiz Silva', 38, '654.123.987-00', 'Rua OO, 9012', 'São Paulo', '12345-678', '(11) 6789-0123', 'luiz.silva@example.com', 'Masculino', 5),
(42, 'Mariana Fernandes', 22, '987.789.123-00', 'Avenida PP, 2345', 'Rio de Janeiro', '23456-789', '(21) 7890-1234', 'mariana.fernandes@example.com', 'Feminino', 3),
(43, 'Gustavo Santos', 36, '321.654.987-00', 'Rua QQ, 5678', 'Belo Horizonte', '34567-890', '(31) 8901-2345', 'gustavo.santos@example.com', 'Masculino', 7),
(44, 'Carolina Oliveira', 28, '789.987.654-00', 'Avenida RR, 9012', 'Brasília', '45678-901', '(61) 9012-3456', 'carolina.oliveira@example.com', 'Feminino', 2),
(45, 'Rafael Rodrigues', 35, '654.321.789-00', 'Rua SS, 1234', 'Salvador', '56789-012', '(71) 0123-4567', 'rafael.rodrigues@example.com', 'Masculino', 4),
(46, 'Vanessa Costa', 23, '987.789.123-00', 'Avenida TT, 2345', 'Recife', '67890-123', '(81) 2345-6789', 'vanessa.costa@example.com', 'Feminino', 1),
(47, 'Marcelo Gomes', 42, '321.987.456-00', 'Rua UU, 5678', 'Porto Alegre', '78901-234', '(51) 3456-7890', 'marcelo.gomes@example.com', 'Masculino', 6),
(48, 'Bianca Almeida', 28, '789.321.987-00', 'Avenida VV, 9012', 'Curitiba', '89012-345', '(41) 4567-8901', 'bianca.almeida@example.com', 'Feminino', 3),
(49, 'Leonardo Lima', 33, '321.654.789-00', 'Rua WW, 1234', 'Fortaleza', '90123-456', '(85) 5678-9012', 'leonardo.lima@example.com', 'Masculino', 2),
(50, 'Fernanda Castro', 27, '789.987.654-00', 'Avenida XX, 5678', 'Manaus', '01234-567', '(92) 6789-0123', 'fernanda.castro@example.com', 'Feminino', 4);

-- --------------------------------------------------------

--
-- Estrutura da tabela `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
CREATE TABLE IF NOT EXISTS `usuarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `login` text NOT NULL,
  `senha` text NOT NULL,
  `nome` text NOT NULL,
  `sobrenome` text NOT NULL,
  `conta` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
--
-- Extraindo dados da tabela `usuarios`
--

INSERT INTO `usuarios` (`id`, `login`, `senha`,`nome`,`sobrenome`,`conta`) VALUES
(1, 'admin', 'admin','admin','admin','administrador'),
(2, 'Pedro', '2023','Pedro','Lima','gerente'),
(3, 'Tiago', '2023','Thiago','Policarpo','gerente'),
(4, 'Marcelo', '0001','Marcelo','Gomes','vendedor'),
(5, 'Joao', '0002','Joao','Silveira','vendedor'),
(6, 'Luana', '0003','Luna','Magalhaes','vendedor')
;


/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;


--
-- Estrutura da tabela `vendas`
--

DROP TABLE IF EXISTS `vendas`;
CREATE TABLE IF NOT EXISTS  `vendas`  (
    `idvenda` int NOT NULL UNIQUE,
    `idcliente` int(11) NOT NULL ,
    `nome` text,
    `cpf` text NOT NULL,
    `idcarro` int(6) NOT NULL,
    `modelo` text,
    `ano` int,
    `cor` text,
    `preco` int,
    `quantidade` int,
    PRIMARY KEY (`idvenda`)
    );

--
-- Inserindo dados da tabela `clientes`
--

INSERT INTO `vendas` (`idvenda`, `idcliente`, `nome`, `cpf`, `idcarro`, `modelo`, `cor`, `ano`, `preco`, `quantidade`)
VALUES (1, 10, 'Patrícia Castro', '789.654.321-00', 18, 'Corolla', 'Azul',2019, 29000, 1),
		(2,  13, 'Gustavo Lima', '321.654.987-00', 6, 'HR-V', 'Prata',2019, 30000, 1),
        (3, 10, 'Patrícia Castro', '789.654.321-00', 15, 'Cruze','Branco',2016,  22000, 2),
       (4, 17, 'Marcelo Gomes', '321.987.456-00', 21, 'HR-V','Prata', 2019, 27000, 1);
       
       
COMMIT;